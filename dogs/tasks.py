from celery import shared_task
from django.core.mail import send_mail
from django.core.management import settings
import requests, datetime

from dogs.models import Dog


@shared_task
def send_message_about_like(message, recipient_email=None, recipient_chat_id=None):
    if recipient_email:
        send_mail(
            subject="Поставлен лайк!",
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[recipient_email, ],
            fail_silently=False,
        )
    if recipient_chat_id:
        URL = 'https://api.telegram.org/bot'
        TOKEN = settings.TELEGRAM_TOKEN
        response = requests.post(
            url=f'{URL}{TOKEN}/sendMessage',
            data={
                'chat_id': recipient_chat_id,
                'text': message,
            }
        )
@shared_task

def send_birthday_mail():
    dog_list = Dog.objects.filter(
        date_born__day=datetime.datetime.now().day,
        date_born__month=datetime.datetime.now().month,
    )
    for dog in dog_list:
        if dog.owner.username:
            URL = 'https://api.telegram.org/bot'
            TOKEN = settings.TELEGRAM_TOKEN
            message=f'поздравляем Вас, {dog.owner.username} c рождением {dog.name}, {datetime.datetime.now()}!'
            response = requests.post(
                url=f'{URL}{TOKEN}/sendMessage',
                data={
                    'chat_id': dog.owner.telegram,
                    'text': message,
                }
            )
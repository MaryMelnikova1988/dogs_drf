# Generated by Django 4.2 on 2024-04-06 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0003_breed_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donation_amount', models.PositiveIntegerField(verbose_name='Сумма пожертовования')),
                ('payment_link', models.URLField(blank=True, max_length=400, null=True, verbose_name='Ссылка на оплату')),
                ('payment_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='id сессии оплаты')),
            ],
            options={
                'verbose_name': 'Пожертвование',
                'verbose_name_plural': 'Пожертвования',
            },
        ),
    ]

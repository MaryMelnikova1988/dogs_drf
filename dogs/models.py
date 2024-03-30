from django.conf import settings
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Breed(models.Model):
    name = models.CharField(max_length=100, verbose_name='Порода')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'
        ordering = ['name',]


class Dog(models.Model):
    name = models.CharField(max_length=250, verbose_name='Кличка')
    breed = models.ForeignKey('dogs.Breed', on_delete=models.CASCADE, **NULLABLE, verbose_name='Порода собаки')
    photo = models.ImageField(upload_to='dog_photo/', **NULLABLE, verbose_name='Фото')
    date_born = models.DateField(**NULLABLE, verbose_name='Дата рождения')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, **NULLABLE, verbose_name='владелец')
    is_public = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.name}, {self.breed}'

    class Meta:
        verbose_name = 'Собака'
        verbose_name_plural = 'Собаки'
        ordering = ['breed', 'name',]
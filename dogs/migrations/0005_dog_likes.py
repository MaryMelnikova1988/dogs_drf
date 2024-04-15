# Generated by Django 4.2 on 2024-04-15 18:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dogs', '0004_donation'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')


class User(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    roles = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER)

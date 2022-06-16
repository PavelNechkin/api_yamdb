from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

from django.db import models


class User(AbstractUser):
    x = [
        ('user', 'user'),
        ('moderator', 'moderator'),
        ('admin', 'admin'),
    ]
    role = models.CharField(max_length=256, choices=x)

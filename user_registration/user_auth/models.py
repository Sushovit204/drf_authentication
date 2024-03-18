from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Model for User where we extend the buit-in user using AbstractUser Class"""
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique = True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
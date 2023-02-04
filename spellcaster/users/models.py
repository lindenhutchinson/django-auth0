from django.db import models
from django.contrib.auth.models import AbstractUser
from characters.models import Character


class User(AbstractUser):
    active_character = models.ForeignKey(Character, on_delete=models.SET_NULL, default=None, null=True, related_name='+')

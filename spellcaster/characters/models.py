from django.db import models
from django.conf import settings
import copy


class Race(models.Model):
    name = models.CharField(max_length=280)
    url = models.CharField(max_length=280)

    def __str__(self):
        return self.name


class ClassType(models.Model):
    name = models.CharField(max_length=280)
    url = models.CharField(max_length=280)
    has_spells = models.BooleanField()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Character(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='characters')
    name = models.CharField(max_length=280)
    level = models.IntegerField()
    class_type = models.ForeignKey(ClassType, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hidden = models.BooleanField(default=False)


class Backstory(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    text = models.TextField()
    title = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

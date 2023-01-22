from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
import copy


class User(AbstractUser):
    pass


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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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


class Spell(models.Model):
    name = models.CharField(max_length=128)
    url = models.CharField(max_length=280)
    # level = models.IntegerField()
    casting_time = models.CharField(max_length=128)
    duration = models.CharField(max_length=128)
    school = models.CharField(max_length=128)
    spell_range = models.CharField(max_length=128)
    components = models.TextField()

    # TODO: these fields should be filled by further scraping
    # source = models.CharField(max_length=256)
    # description = models.TextField()
    # at_higher_levels = models.TextField()

    classes = models.ManyToManyField(ClassType, through="SpellClass")


class SpellClass(models.Model):
    spell = models.ForeignKey(Spell, on_delete=models.CASCADE)
    class_type = models.ForeignKey(ClassType, on_delete=models.CASCADE)


class CharacterSpell(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    spell = models.ForeignKey(Spell, on_delete=models.CASCADE)
    prepared = models.BooleanField()
    costs_slot = models.BooleanField()


class SpellSlot(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    level = models.IntegerField()
    slots_remaining = models.IntegerField(default=0)


class SpellSlotProgression(models.Model):
    class_type = models.ForeignKey(ClassType, on_delete=models.CASCADE)
    spell_level = models.IntegerField()
    slots_at_level = models.IntegerField()


class CastSpell(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    spell = models.ForeignKey(Spell, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # other fields to store information about the spell cast
    pass

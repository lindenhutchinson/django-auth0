from django import forms
from .models import Character, Race, ClassType


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ["name", "level", "race", "class_type"]

    # Restrict the race and class_type fields to the choices in the database
    race = forms.ModelChoiceField(queryset=Race.objects.all())
    class_type = forms.ModelChoiceField(queryset=ClassType.objects.all())

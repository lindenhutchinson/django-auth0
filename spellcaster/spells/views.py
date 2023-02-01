from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, get_user_model
from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required
from .models import Spell
from users.models import User
from django.db.models import Count
from datetime import datetime
from django.http import JsonResponse

SPELL_TABLE_HEADERS = {
    "name": {"display": "Name", "class": "center-td widthy-td"},
    "level": {"display": "Level", "class": "center-td"},
    "school": {"display": "School", "class": "center-td"},
    "casting_time": {"display": "Casting Time", "class": "center-td"},
    "spell_range": {"display": "Range", "class": "center-td"},
    # "components": {"display": "Components", "class": "center-td"},
    # "duration": {"display": "Duration", "class": "widthy-td"},
}


@login_required
def spell_description(request, spell_id):
    spell = Spell.objects.get(id=spell_id)
    return JsonResponse({"description": spell.description})

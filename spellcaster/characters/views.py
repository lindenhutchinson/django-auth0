from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, get_user_model
from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required
from .models import Character, ClassType
from spells.models import Spell
from users.models import User
from django.db.models import Count
from datetime import datetime
from .forms import CharacterForm
from .utils import create_spell_slots
from .tables import CharacterTable
from django.http import JsonResponse
from django.core.paginator import Paginator

SPELL_TABLE_HEADERS = {
    "name": {"display": "Name", "class": "widthy-td"},
    "level": {"display": "Level", "class": "center-td"},
    "school": {"display": "School", "class": ""},
    "casting_time": {"display": "Casting Time", "class": ""},
    "spell_range": {"display": "Range", "class": ""},
    # "components": {"display": "Components", "class": "center-td"},
    # "duration": {"display": "Duration", "class": "widthy-td"},
}

PAGINATION_SPELLS_PER_PAGE = 15


@login_required
def character_detail(request, pk):
    character = Character.objects.filter(pk=pk).first()
    if request.user != character.user:
        return redirect("forbidden")

    request.user.active_character = character
    request.user.save()

    context = {
        "char": character,
    }
    return render(request, "character_detail.html", context)


@login_required
def character_edit(request, pk):
    character = Character.objects.get(pk=pk)
    if request.user != character.user:
        # Redirect unauthorized users to a 403 page or to login page
        return redirect("forbidden")
    if request.method == "POST":
        form = CharacterForm(request.POST, instance=character)
        if form.is_valid():
            form.save()
            return redirect("character_list")
    else:
        form = CharacterForm(instance=character)

    context = {"form": form}
    return render(request, "character_create.html", context)


@login_required
def character_delete(request, pk):
    character = Character.objects.get(pk=pk)
    if request.user != character.user:
        # Redirect unauthorized users to a 403 page or to login page
        return redirect("forbidden")

    character.delete()
    return redirect("character_list")


@login_required
def character_list(request):
    data = Character.objects.filter(user=request.user).order_by("updated_at").reverse()
    table = CharacterTable(data)
    table.paginate(page=request.GET.get("page", 1), per_page=5)

    return render(request, "character_list.html", {"table": table})


@login_required
def character_create(request):
    if request.method == "POST":
        form = CharacterForm(request.POST)
        if form.is_valid():
            character = form.save(commit=False)
            character.user = request.user
            character.save()
            create_spell_slots(character)

            return redirect("character_list")
    else:
        form = CharacterForm()
    return render(request, "character_create.html", {"form": form})


@login_required
def set_active_character(request, pk):
    # Get the character that the user wants to set as active
    character = Character.objects.get(id=pk)
    if request.user != character.user:
        return redirect("forbidden")

    prev_char = request.user.active_character
    # Set the active character for the user
    request.user.active_character = character
    request.user.save()
    return JsonResponse({"new": character.id, "old": prev_char.id})

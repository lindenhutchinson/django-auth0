from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, get_user_model
from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required
from .models import User, Character, Spell
from django.db.models import Count
from datetime import datetime
from .forms import CharacterForm
from .utils import create_spell_slots
from .tables import CharacterTable
from django.http import JsonResponse
from django.core.paginator import Paginator


def index(request):
    return render(request, "feedapp/index.html")


@login_required
def character_detail(request, pk):
    character = Character.objects.filter(pk=pk).first()
    if request.user != character.user:
        return redirect("forbidden")
    search_term = request.GET.get('search', '')
    spells = Spell.objects.filter(name__icontains=search_term)
    # Create a paginator object with a specified number of items per page
    paginator = Paginator(spells, 10)
    # Get the current page number from the request
    page_number = request.GET.get("page")

    # Get the spells for the current page
    spells = paginator.get_page(page_number)
    context = {"char": character, "spells": spells, 'search_term': search_term}
    return render(request, "feedapp/character_detail.html", context)


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
    return render(request, "feedapp/character_create.html", context)


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
    data = Character.objects.filter(user=request.user).order_by("created_at").reverse()
    table = CharacterTable(data)
    table.paginate(page=request.GET.get("page", 1), per_page=5)

    return render(request, "feedapp/character_list.html", {"table": table})


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
    return render(request, "feedapp/character_create.html", {"form": form})


@login_required
def logout(request):
    django_logout(request)
    domain = settings.SOCIAL_AUTH_AUTH0_DOMAIN
    client_id = settings.SOCIAL_AUTH_AUTH0_KEY
    return_to = "http://127.0.0.1:8000"  # this can be current domain
    return redirect(
        f"https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}"
    )


@login_required
def spell_description(request, spell_id):
    spell = Spell.objects.get(id=spell_id)
    return JsonResponse({"description": spell.description})

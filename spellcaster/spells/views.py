from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, get_user_model
from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required
from .models import Character, ClassType
from spells.models import Spell
from users.models import User
from django.db.models import Count
from datetime import datetime
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
def spell_table(request):
    spells = Spell.objects.all()

    if search_term := request.GET.get("search", ""):
        spells = Spell.objects.filter(name__icontains=search_term)
    if class_filter := request.GET.get("class", ""):
        spells = spells.filter(classes__name__exact=class_filter)
    if school_filter := request.GET.get("school", ""):
        spells = spells.filter(school__exact=school_filter)
    if level_filter := request.GET.get("level", ""):
        spells = spells.filter(level__exact=level_filter)

    sort = request.GET.get("sort", "")
    order = request.GET.get("order", "")
    if sort and order:
        spells = spells.order_by(f"{'-' if order == 'desc' else ''}{sort}")
    else:
        spells = spells.order_by("name")

    # Get all unique classes, schools, and levels
    classes = (
        ClassType.objects.filter(has_spells=True)
        .values_list("name", flat=True)
        .distinct()
    )
    schools = Spell.objects.values_list("school", flat=True).distinct()
    levels = Spell.objects.values_list("level", flat=True).distinct()

    num_spells = spells.count

    paginator = Paginator(spells, PAGINATION_SPELLS_PER_PAGE)
    page = request.GET.get("page")
    spells = paginator.get_page(page)
    context = {
        "spells": spells,
        "classes": classes,
        "schools": schools,
        "levels": levels,
        "search_term": search_term,
        "class_filter": class_filter,
        "school_filter": school_filter,
        "level_filter": level_filter,
        "num_spells": num_spells,
        "sort": sort,
        "order": order,
        "table_headers": SPELL_TABLE_HEADERS,
    }
    return render(request, "spell_table.html", context)


@login_required
def spell_description(request, spell_id):
    spell = Spell.objects.get(id=spell_id)
    return render(request, 'spell_description.html', {'spell': spell})


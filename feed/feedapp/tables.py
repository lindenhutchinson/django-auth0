import django_tables2 as tables
from django.urls import reverse
from django.utils.html import format_html
from .models import Character


class CharacterTable(tables.Table):
    class Meta:
        attrs = {"class": "table"}
        model = Character
        fields = ("name", "level", "class_type", "race", "actions")

    name = tables.LinkColumn(
        verbose_name="Name", viewname="character_detail", args=[tables.A("pk")]
    )
    level = tables.Column(verbose_name="Level")
    class_type = tables.Column(verbose_name="Class")
    race = tables.Column(verbose_name="Race")
    actions = tables.TemplateColumn(
        template_name="feedapp/character_actions.html", verbose_name="Actions"
    )

from django import template

register = template.Library()


@register.filter
def in_character_spells(character, spell_id):
    return character.spells.filter(spell__id=spell_id).exists()

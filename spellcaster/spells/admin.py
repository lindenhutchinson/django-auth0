from django.contrib import admin

# Register your models here.
from .models import Spell, SpellClass, CharacterSpell, SpellSlot, SpellSlotProgression, CastSpell

admin.site.register(Spell)
admin.site.register(SpellClass)
admin.site.register(CharacterSpell)
admin.site.register(SpellSlot)
admin.site.register(SpellSlotProgression)
admin.site.register(CastSpell)

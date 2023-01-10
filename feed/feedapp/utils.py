def create_spell_slots(character):
    # get the highest level class that has spell slots for the character
    highest_level_class = character.class_type.exclude(has_spells=0).order_by('-level').first()
    if highest_level_class:
        spell_slot_progression = SpellSlotProgression.objects.filter(class_type=highest_level_class)
        for progression in spell_slot_progression:
            SpellSlot.objects.create(character=character, spell_level=progression.spell_level, slots_remaining=progression.slots_at_level)
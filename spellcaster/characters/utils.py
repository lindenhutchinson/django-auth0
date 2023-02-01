from spells.models import SpellSlot, SpellSlotProgression


def create_spell_slots(character):
    # get the highest level class that has spell slots for the character
    spell_class = character.class_type

    spell_slot_progression = SpellSlotProgression.objects.filter(
        class_type=spell_class, spell_level=character.level
    )
    spell_slots = []
    for i, progression in enumerate(spell_slot_progression):
        if progression:
            spell_slots.append(
                SpellSlot(
                    character=character,
                    level=i + 1,
                    slots_remaining=progression.slots_at_level,
                )
            )

    if len(spell_slots):
        SpellSlot.objects.bulk_create(spell_slots)

# Generated by Django 4.1.5 on 2023-01-10 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("feedapp", "0005_spell_url"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="spell",
            name="level",
        ),
    ]
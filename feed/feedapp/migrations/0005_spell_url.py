# Generated by Django 4.1.5 on 2023-01-10 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("feedapp", "0004_alter_spellslotprogression_class_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="spell",
            name="url",
            field=models.CharField(default=0, max_length=280),
            preserve_default=False,
        ),
    ]
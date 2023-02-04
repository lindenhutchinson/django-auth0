# Generated by Django 4.1.5 on 2023-02-04 05:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("characters", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="character",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="characters",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]

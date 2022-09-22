# Generated by Django 4.1.1 on 2022-09-15 19:21

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Programme_immobilier",
            fields=[
                (
                    "nom_prog",
                    models.CharField(
                        max_length=100, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("is_active", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="Appartement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("surface", models.FloatField()),
                ("prix", models.FloatField()),
                ("nombre_piece", models.IntegerField()),
                (
                    "list_caracteristiques",
                    multiselectfield.db.fields.MultiSelectField(
                        choices=[
                            ("Proche station ski", "Proche station ski"),
                            ("Piscine", "Piscine"),
                            ("Jardin", "Jardin"),
                            ("Cave", "Cave"),
                            ("Parking", "Parking"),
                        ],
                        max_length=200,
                    ),
                ),
                (
                    "program",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="prog_immobilier.programme_immobilier",
                    ),
                ),
            ],
        ),
    ]
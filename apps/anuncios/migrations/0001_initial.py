# Generated by Django 4.2.1 on 2023-10-23 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Personal",
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
                ("cedula", models.CharField(max_length=8)),
                ("nombre", models.CharField(max_length=100)),
                ("apellido", models.CharField(max_length=100)),
                ("cargo", models.CharField(max_length=100)),
                ("fecha_ingreso", models.DateField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Personal",
                "verbose_name_plural": "Personal",
            },
        ),
        migrations.CreateModel(
            name="Anuncios",
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
                (
                    "fecha_actualizacion",
                    models.DateField(auto_created=True, auto_now=True, null=True),
                ),
                (
                    "fecha_publicacion",
                    models.DateField(auto_created=True, auto_now=True, null=True),
                ),
                ("titulo", models.CharField(blank=True, max_length=150, null=True)),
                (
                    "imagen",
                    models.ImageField(blank=True, null=True, upload_to="anuncios"),
                ),
                ("descripcion", models.TextField(blank=True, null=True)),
                (
                    "autor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="anuncios.personal",
                    ),
                ),
            ],
            options={
                "verbose_name": "Anuncio",
                "verbose_name_plural": "Anuncios",
            },
        ),
    ]
# Generated by Django 4.2 on 2023-10-23 19:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Usuario",
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
                ("nombre", models.CharField(max_length=50)),
                ("apellido", models.CharField(max_length=50)),
                ("cedula", models.CharField(max_length=10)),
                ("telefono", models.CharField(max_length=16)),
                ("telefono2", models.CharField(blank=True, max_length=16, null=True)),
                ("direccion", models.TextField(blank=True, null=True)),
                ("cargo", models.CharField(max_length=100)),
                ("fecha_ingreso", models.DateField(blank=True, null=True)),
                (
                    "especialidad",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("horario_inicio", models.TimeField(blank=True, null=True)),
                ("horario_final", models.TimeField(blank=True, null=True)),
                (
                    "tipo_usuario",
                    models.CharField(
                        choices=[("AD", "Admin"), ("ME", "Medico"), ("CL", "Cliente")],
                        default="CL",
                        max_length=2,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Usuario",
                "verbose_name_plural": "Usuarios",
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
                        to="anuncios.usuario",
                    ),
                ),
            ],
            options={
                "verbose_name": "Anuncio",
                "verbose_name_plural": "Anuncios",
            },
        ),
    ]

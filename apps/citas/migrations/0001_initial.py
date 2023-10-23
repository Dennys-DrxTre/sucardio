# Generated by Django 4.2.1 on 2023-10-23 04:05

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
                ("nombre_pac", models.CharField(max_length=50)),
                ("apellido_pac", models.CharField(max_length=50)),
                ("cedula_pac", models.CharField(max_length=10)),
                ("telefono", models.CharField(max_length=16)),
                ("telefono2", models.CharField(blank=True, max_length=16, null=True)),
                ("direccion", models.TextField()),
                ("profesion", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "especialidad",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("horario", models.CharField(blank=True, max_length=150, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Cliente",
                "verbose_name_plural": "Clientes",
            },
        ),
        migrations.CreateModel(
            name="Cita",
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
                ("control_pac", models.BooleanField(default=False)),
                ("fecha_cita", models.DateField(blank=True, null=True)),
                ("motivo_consulta", models.TextField()),
                ("metodo_pago", models.CharField(max_length=20)),
                (
                    "medico",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="citas.usuario"
                    ),
                ),
            ],
            options={
                "verbose_name": "Cita",
                "verbose_name_plural": "Citas",
            },
        ),
    ]

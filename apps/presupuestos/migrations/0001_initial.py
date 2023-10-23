# Generated by Django 4.2 on 2023-10-23 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("anuncios", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Servicio",
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
                ("nombre_serv", models.CharField(max_length=50)),
                ("descripcion", models.TextField(blank=True, null=True)),
                ("precio_serv", models.FloatField(default=0.0)),
                ("metodo_pago", models.CharField(max_length=20)),
                (
                    "medico",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="anuncios.usuario",
                    ),
                ),
            ],
            options={
                "verbose_name": "Servicio",
                "verbose_name_plural": "Servicios",
            },
        ),
        migrations.CreateModel(
            name="Presupuesto",
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
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="anuncios.usuario",
                    ),
                ),
                (
                    "servicio",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="presupuestos.servicio",
                    ),
                ),
            ],
            options={
                "verbose_name": "Presupuesto",
                "verbose_name_plural": "Presupuestos",
            },
        ),
    ]

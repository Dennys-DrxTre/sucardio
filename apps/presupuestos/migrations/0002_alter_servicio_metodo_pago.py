# Generated by Django 4.2 on 2023-11-05 02:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("presupuestos", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="servicio",
            name="metodo_pago",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
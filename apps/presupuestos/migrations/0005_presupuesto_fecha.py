# Generated by Django 4.2 on 2023-11-05 17:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("presupuestos", "0004_remove_presupuesto_servicio_presupuesto_total_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="presupuesto",
            name="fecha",
            field=models.DateField(default=datetime.date.today),
        ),
    ]

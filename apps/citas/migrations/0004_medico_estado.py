# Generated by Django 4.2 on 2023-10-29 20:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("citas", "0003_alter_cita_medico"),
    ]

    operations = [
        migrations.AddField(
            model_name="medico",
            name="estado",
            field=models.CharField(
                choices=[("AC", "Habilitado"), ("DE", "Desabilitado")],
                default="AC",
                max_length=2,
            ),
        ),
    ]

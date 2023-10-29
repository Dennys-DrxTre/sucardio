# Generated by Django 4.2 on 2023-10-29 19:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("anuncios", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="anuncios",
            name="estado",
            field=models.CharField(
                choices=[("AC", "Habilitado"), ("DE", "Desabilitado")],
                default="AC",
                max_length=2,
            ),
        ),
        migrations.AlterField(
            model_name="usuario",
            name="telefono",
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name="usuario",
            name="telefono2",
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]

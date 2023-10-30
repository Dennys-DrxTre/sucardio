# Generated by Django 4.2 on 2023-10-29 19:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("citas", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="cita",
            name="estado",
            field=models.CharField(
                choices=[("AC", "Habilitado"), ("DE", "Desabilitado")],
                default="AC",
                max_length=2,
            ),
        ),
        migrations.AlterField(
            model_name="medico",
            name="especialidad",
            field=models.CharField(
                choices=[
                    ("Nefrologo", "Nefrologo"),
                    ("Neurologo", "Neurologo"),
                    ("Cardiologo clinico", "Cardiologo clinico"),
                    ("Cardiologo hemodinamista", "Cardiologo hemodinamista"),
                    ("Cardiologo arritmiologo", "Cardiologo arritmiologo"),
                    ("Cardiologo Pediatra", "Cardiologo Pediatra"),
                    ("Neumonologo", "Neumonologo"),
                    ("Neumonologo pediatra", "Neumonologo pediatra"),
                    (
                        "Medico internista y diabetologo",
                        "Medico internista y diabetologo",
                    ),
                    ("Medico emergenciologo", "Medico emergenciologo"),
                    ("Medico general", "Medico general"),
                    ("Medico cirujano", "Medico cirujano"),
                    ("Medico ocupacional", "Medico ocupacional"),
                    ("Medio urologo", "Medio urologo"),
                    ("Medico gastroenterologo", "Medico gastroenterologo"),
                    ("Medico otorrinolaringologo", "Medico otorrinolaringologo"),
                    ("Medico Angiologo", "Medico Angiologo"),
                    ("Medico imagenologo", "Medico imagenologo"),
                    (
                        "Medico cirujano especialista en manos",
                        "Medico cirujano especialista en manos",
                    ),
                    ("Medico traumatologo", "Medico traumatologo"),
                ],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="medico",
            name="telefono",
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name="medico",
            name="telefono2",
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
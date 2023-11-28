# Generated by Django 4.2 on 2023-11-28 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("anuncios", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Medico",
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
                ("telefono", models.CharField(max_length=11)),
                ("telefono2", models.CharField(blank=True, max_length=11, null=True)),
                ("direccion", models.TextField(blank=True, null=True)),
                (
                    "nacionalidad",
                    models.CharField(
                        blank=True,
                        choices=[("E", "E"), ("V", "V")],
                        default="V",
                        max_length=2,
                        null=True,
                    ),
                ),
                (
                    "estado",
                    models.CharField(
                        blank=True,
                        choices=[("AC", "Habilitado"), ("DE", "Deshabilitado")],
                        default="AC",
                        max_length=2,
                        null=True,
                    ),
                ),
                ("fecha_ingreso", models.DateField(blank=True, null=True)),
                (
                    "especialidad",
                    models.CharField(
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
                            (
                                "Medico otorrinolaringologo",
                                "Medico otorrinolaringologo",
                            ),
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
                ("horario_inicio", models.TimeField(blank=True, null=True)),
                ("horario_final", models.TimeField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Medico",
                "verbose_name_plural": "Medicos",
                "permissions": [],
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
                (
                    "metodo_pago",
                    models.CharField(
                        choices=[
                            ("Pago móvil", "Pago móvil"),
                            ("Transferencia", "Transferencia"),
                            ("Zelle", "Zelle"),
                            ("Débito", "Débito"),
                            ("Efectivo BS", "Efectivo BS"),
                            ("Efectivo Dólares", "Efectivo Dólares"),
                            ("Efectivo Euros", "Efectivo Euros"),
                        ],
                        max_length=30,
                    ),
                ),
                (
                    "estado",
                    models.CharField(
                        choices=[
                            ("PE", "Pendiente"),
                            ("AP", "Aprobado"),
                            ("RE", "Rechazado"),
                        ],
                        default="PE",
                        max_length=20,
                    ),
                ),
                ("notificado", models.BooleanField(default=False)),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="anuncios.usuario",
                    ),
                ),
                (
                    "medico",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="citas.medico"
                    ),
                ),
            ],
            options={
                "verbose_name": "Cita",
                "verbose_name_plural": "Citas",
                "permissions": [],
            },
        ),
    ]

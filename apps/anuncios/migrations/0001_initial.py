# Generated by Django 4.2 on 2023-11-28 23:37

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
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_registro', models.DateField(auto_created=True, blank=True, null=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('cedula', models.CharField(max_length=10)),
                ('telefono', models.CharField(max_length=11)),
                ('telefono2', models.CharField(blank=True, max_length=11, null=True)),
                ('direccion', models.TextField(blank=True, null=True)),
                ('nacionalidad', models.CharField(blank=True, choices=[('E', 'E'), ('V', 'V')], default='V', max_length=2, null=True)),
                ('tipo_usuario', models.CharField(choices=[('AD', 'Admin'), ('SE', 'Secretaria'), ('CL', 'Cliente')], default='CL', max_length=2)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'permissions': [('requiere_usuario', 'requiero nivel usuario'), ('requiere_secretria', 'requiero nivel secretaria'), ('requiere_admin', 'requiero nivel admin')],
            },
        ),
        migrations.CreateModel(
            name='Anuncios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_actualizacion', models.DateField(auto_created=True, auto_now=True, null=True)),
                ('fecha_publicacion', models.DateField(auto_created=True, auto_now=True, null=True)),
                ('estado', models.CharField(blank=True, choices=[('AC', 'Habilitado'), ('DE', 'Desabilitado')], default='AC', max_length=2, null=True)),
                ('titulo', models.CharField(blank=True, max_length=150, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='anuncios')),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='anuncios.usuario')),
            ],
            options={
                'verbose_name': 'Anuncio',
                'verbose_name_plural': 'Anuncios',
                'permissions': [],
            },
        ),
    ]

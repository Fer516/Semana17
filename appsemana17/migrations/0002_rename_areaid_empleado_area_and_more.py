# Generated by Django 4.2.7 on 2023-11-12 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appsemana17', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='areaId',
            new_name='area',
        ),
        migrations.RenameField(
            model_name='venta',
            old_name='clienteId',
            new_name='cliente',
        ),
        migrations.RenameField(
            model_name='venta',
            old_name='empleadoId',
            new_name='empleado',
        ),
    ]
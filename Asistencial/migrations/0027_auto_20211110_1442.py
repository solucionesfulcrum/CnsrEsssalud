# Generated by Django 3.1.1 on 2021-11-10 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Asistencial', '0026_auto_20211110_1441'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personal',
            old_name='datosDependencia',
            new_name='dependencia',
        ),
        migrations.RemoveField(
            model_name='personal',
            name='areaPer',
        ),
    ]
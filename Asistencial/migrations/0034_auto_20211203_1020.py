# Generated by Django 3.1.1 on 2021-12-03 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Asistencial', '0033_auto_20211203_0907'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incidenciadsi',
            old_name='estado',
            new_name='maestro',
        ),
    ]
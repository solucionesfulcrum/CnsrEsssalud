# Generated by Django 3.1.1 on 2023-01-13 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asistencial', '0047_auto_20230113_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidenciadsi',
            name='userReg',
            field=models.CharField(max_length=200),
        ),
    ]
# Generated by Django 3.1.1 on 2022-05-23 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asistencial', '0003_auto_20220520_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cas',
            name='descripCas',
            field=models.CharField(max_length=100),
        ),
    ]

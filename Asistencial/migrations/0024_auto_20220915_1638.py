# Generated by Django 3.1.1 on 2022-09-15 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asistencial', '0023_nutricion_circubra'),
    ]

    operations = [
        migrations.AddField(
            model_name='nutricion',
            name='ingestaCaloricaT',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nutricion',
            name='ingestaProteicaT',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]
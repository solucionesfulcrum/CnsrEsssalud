# Generated by Django 3.1.1 on 2022-12-15 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asistencial', '0036_auto_20221118_0858'),
    ]

    operations = [
        migrations.AddField(
            model_name='nutricion',
            name='tipoPaciente',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
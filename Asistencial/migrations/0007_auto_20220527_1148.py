# Generated by Django 3.1.1 on 2022-05-27 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Asistencial', '0006_cas_tipocas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='casOri',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Asistencial.cas'),
        ),
    ]

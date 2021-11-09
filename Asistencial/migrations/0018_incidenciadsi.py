# Generated by Django 3.1.1 on 2021-11-08 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Asistencial', '0017_auto_20211028_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='incidenciaDsi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=50)),
                ('clasiSolu', models.CharField(max_length=50)),
                ('solucion', models.CharField(max_length=500)),
                ('ambiente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Asistencial.ambiente')),
                ('personal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Asistencial.personal')),
            ],
        ),
    ]

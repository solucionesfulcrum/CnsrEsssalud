# Generated by Django 3.1.1 on 2022-03-08 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Asistencial', '0044_biendetallemonitor'),
    ]

    operations = [
        migrations.CreateModel(
            name='nutricion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diaTurno', models.CharField(max_length=30)),
                ('fechaIngreso', models.DateField()),
                ('fechaEvaluacion', models.DateField()),
                ('peso', models.CharField(max_length=30)),
                ('talla', models.CharField(max_length=30)),
                ('imc', models.CharField(max_length=30)),
                ('porcentajeCMB', models.CharField(max_length=30)),
                ('porcentajeEPT', models.CharField(max_length=30)),
                ('albSerica', models.CharField(max_length=30)),
                ('ValGlobalSub', models.CharField(max_length=30)),
                ('ingestaCalorica', models.CharField(max_length=60)),
                ('ingestaProteica', models.CharField(max_length=60)),
                ('diagNutricional', models.CharField(max_length=60)),
                ('interveNutricional', models.CharField(max_length=60)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Asistencial.paciente')),
            ],
        ),
    ]

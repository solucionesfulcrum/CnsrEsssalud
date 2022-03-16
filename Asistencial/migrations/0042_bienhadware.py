# Generated by Django 3.1.1 on 2022-03-03 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Asistencial', '0041_admianemia_exclusionanemia_movimientoanemia_presanemia'),
    ]

    operations = [
        migrations.CreateModel(
            name='bienHadware',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procesador', models.CharField(max_length=20)),
                ('numeroIp', models.CharField(max_length=20)),
                ('numeroMac', models.CharField(max_length=20)),
                ('memoriaRam', models.CharField(max_length=20)),
                ('capAlmacenamiento', models.CharField(max_length=20)),
                ('uso', models.CharField(max_length=20)),
                ('condicion', models.CharField(max_length=20)),
                ('bienpat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Asistencial.bienpat')),
            ],
        ),
    ]
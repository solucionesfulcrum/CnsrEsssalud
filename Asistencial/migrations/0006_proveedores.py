# Generated by Django 3.1.1 on 2021-10-27 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asistencial', '0005_auto_20211026_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='proveedores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rucProveedor', models.CharField(max_length=30, unique=True)),
                ('nombreProveedor', models.CharField(max_length=50)),
                ('telefProveedor', models.CharField(max_length=20)),
                ('direcProveedor', models.CharField(max_length=20, null=True)),
                ('estadoProveedor', models.CharField(default=1, max_length=5)),
            ],
        ),
    ]
# Generated by Django 3.1.1 on 2023-03-13 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asistencial', '0050_paramecentropuesto'),
    ]

    operations = [
        migrations.AddField(
            model_name='paramecentropuesto',
            name='numeroPuesto',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
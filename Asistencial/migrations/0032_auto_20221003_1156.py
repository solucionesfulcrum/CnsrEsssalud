# Generated by Django 3.1.1 on 2022-10-03 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asistencial', '0031_auto_20220928_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='delegacionbienesestra',
            name='cantiRequeridaUsu',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='delegacionbienesestra',
            name='obsUsu',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

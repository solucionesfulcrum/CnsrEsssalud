# Generated by Django 3.1.1 on 2021-10-27 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Asistencial', '0011_remove_provmaq_bienpat'),
    ]

    operations = [
        migrations.AddField(
            model_name='provmaq',
            name='bienpat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Asistencial.bienpat'),
            preserve_default=False,
        ),
    ]

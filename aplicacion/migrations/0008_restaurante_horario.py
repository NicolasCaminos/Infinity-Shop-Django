# Generated by Django 4.2.3 on 2023-08-12 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0007_restaurante_calificacion_restaurante_capacidad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurante',
            name='horario',
            field=models.TimeField(default='00:00'),
            preserve_default=False,
        ),
    ]
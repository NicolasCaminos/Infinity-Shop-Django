# Generated by Django 4.2.7 on 2023-11-24 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppInfinity', '0002_producto_precio_alter_producto_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='precio',
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
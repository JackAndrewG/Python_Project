# Generated by Django 2.2.1 on 2019-07-05 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20190705_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancha',
            name='descripcion_cancha',
            field=models.CharField(default='Cancha de fútbol Nro 1', max_length=200),
        ),
    ]

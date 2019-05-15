# Generated by Django 2.2.1 on 2019-05-15 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20190514_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='cancha',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Cancha'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='codigo_reserva',
            field=models.CharField(default='000123', max_length=6),
        ),
    ]

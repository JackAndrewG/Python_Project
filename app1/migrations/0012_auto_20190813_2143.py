# Generated by Django 2.2.1 on 2019-08-14 02:43

import app1.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_auto_20190813_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancha',
            name='foto_cancha',
            field=models.ImageField(blank=True, null=True, upload_to='images/canchas_images', validators=[app1.validators.valid_extension]),
        ),
    ]

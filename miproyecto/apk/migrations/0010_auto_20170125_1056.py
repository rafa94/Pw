# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apk', '0009_auto_20170124_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugadores',
            name='imagen',
            field=models.ImageField(default='', upload_to='apk/static/imagenes/'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apk', '0003_auto_20170121_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipo',
            name='jugadores',
        ),
        migrations.AddField(
            model_name='equipo',
            name='jugadores',
            field=models.ManyToManyField(to='apk.Jugadores'),
        ),
    ]

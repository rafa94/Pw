# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apk', '0021_partidos_arbitro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partidos',
            name='jornada',
        ),
        migrations.AddField(
            model_name='equipo',
            name='GC',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='equipo',
            name='GF',
            field=models.IntegerField(default=0),
        ),
    ]

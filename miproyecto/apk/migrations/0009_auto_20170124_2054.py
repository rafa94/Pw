# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 19:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apk', '0008_auto_20170124_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='jugadores',
            name='imagen',
            field=models.ImageField(default='', upload_to='static/imagenes/'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='nombre',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.RemoveField(
            model_name='jugadores',
            name='equipo',
        ),
        migrations.AddField(
            model_name='jugadores',
            name='equipo',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='apk.Equipo'),
        ),
        migrations.AlterField(
            model_name='jugadores',
            name='nombre',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='jugadores',
            name='posicion',
            field=models.CharField(default='', max_length=15),
        ),
    ]

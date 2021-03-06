# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 12:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apk', '0002_auto_20170120_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('clasificacion', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Jugadores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('posicion', models.CharField(max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='Clasificacion',
        ),
        migrations.DeleteModel(
            name='Equipos',
        ),
        migrations.AddField(
            model_name='equipo',
            name='jugadores',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apk.Jugadores'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 12:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apk', '0004_auto_20170121_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posicion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apk.Equipo')),
            ],
        ),
    ]

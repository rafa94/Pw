# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 12:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apk', '0014_auto_20170125_1222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jugadores',
            name='imagen',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-21 07:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20170921_0729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='line',
        ),
        migrations.AddField(
            model_name='profile',
            name='m1',
            field=models.ManyToManyField(to='cms.line'),
        ),
    ]

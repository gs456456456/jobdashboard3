# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-21 07:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.AddField(
            model_name='line',
            name='num',
            field=models.CharField(default=1, max_length=10, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='line',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cms.line', to_field='num'),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-31 18:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0003_auto_20180130_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

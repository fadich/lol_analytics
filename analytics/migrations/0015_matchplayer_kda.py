# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-09 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0014_delete_analyticscache'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchplayer',
            name='kda',
            field=models.FloatField(null=True),
        ),
    ]
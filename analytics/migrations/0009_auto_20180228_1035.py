# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-28 10:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0008_auto_20180228_1019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='lane',
        ),
        migrations.RemoveField(
            model_name='match',
            name='role',
        ),
        migrations.AddField(
            model_name='matchplayer',
            name='lane',
            field=models.CharField(default=0, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='matchplayer',
            name='role',
            field=models.CharField(default=0, max_length=32),
            preserve_default=False,
        ),
    ]

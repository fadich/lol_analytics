# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-06 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0011_auto_20180306_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchplayer',
            name='largest_killing_spree',
            field=models.SmallIntegerField(null=True),
        ),
    ]

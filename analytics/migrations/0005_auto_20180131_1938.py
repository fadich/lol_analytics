# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-31 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0004_account_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='updated_at',
            field=models.DateTimeField(),
        ),
    ]

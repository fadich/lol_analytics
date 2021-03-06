# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-30 00:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('server', models.CharField(max_length=32)),
                ('account_id', models.IntegerField()),
                ('summoner_id', models.IntegerField()),
                ('icon_id', models.IntegerField()),
                ('summoner_level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Champion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('champion_id', models.IntegerField()),
                ('name', models.CharField(max_length=128)),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform_id', models.CharField(max_length=32)),
                ('game_id', models.BigIntegerField()),
                ('queue', models.IntegerField()),
                ('season', models.BigIntegerField()),
                ('timestamp', models.IntegerField()),
                ('role', models.CharField(max_length=32)),
                ('lane', models.CharField(max_length=32)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analytics.Account')),
                ('champion', models.ManyToManyField(to='analytics.Champion')),
            ],
        ),
    ]

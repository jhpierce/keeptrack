# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-25 22:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0040_auto_20161223_1616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crosstrain',
            name='activity',
        ),
        migrations.RemoveField(
            model_name='event',
            name='activity',
        ),
        migrations.RemoveField(
            model_name='event',
            name='meet',
        ),
        migrations.RemoveField(
            model_name='intervalrun',
            name='activity',
        ),
        migrations.RemoveField(
            model_name='normalrun',
            name='activity',
        ),
        migrations.RemoveField(
            model_name='rep',
            name='interval_run',
        ),
        migrations.DeleteModel(
            name='CrossTrain',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='IntervalRun',
        ),
        migrations.DeleteModel(
            name='NormalRun',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-12 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0030_activity_user_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='calendarId',
            field=models.CharField(default='primary', max_length=200),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-15 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0031_team_calendarid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='default_location',
            field=models.CharField(default=b'Kirkland, NY', max_length=50),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-20 02:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0033_auto_20161120_0222'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoe',
            name='athlete',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='log.Athlete'),
            preserve_default=False,
        ),
    ]

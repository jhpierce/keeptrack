# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-30 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0038_auto_20161122_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='phone_number',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-18 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0018_auto_20161015_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='intervalrun',
            name='units',
            field=models.CharField(choices=[(b'Miles', b'Miles'), (b'Meters', b'Meters'), (b'Kilometers', b'Kilometers')], default=b'Miles', max_length=12),
        ),
    ]
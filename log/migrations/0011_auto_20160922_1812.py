# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-22 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0010_auto_20160922_0255'),
    ]

    operations = [
        migrations.AddField(
            model_name='crosstrain',
            name='units',
            field=models.CharField(choices=[(b'Miles', b'Miles'), (b'Meters', b'Meters'), (b'Kilometers', b'Kilometers')], default=b'Miles', max_length=12),
        ),
        migrations.AddField(
            model_name='event',
            name='units',
            field=models.CharField(choices=[(b'Miles', b'Miles'), (b'Meters', b'Meters'), (b'Kilometers', b'Kilometers')], default=b'Miles', max_length=12),
        ),
        migrations.AddField(
            model_name='normalrun',
            name='units',
            field=models.CharField(choices=[(b'Miles', b'Miles'), (b'Meters', b'Meters'), (b'Kilometers', b'Kilometers')], default=b'Miles', max_length=12),
        ),
        migrations.AddField(
            model_name='rep',
            name='units',
            field=models.CharField(choices=[(b'Miles', b'Miles'), (b'Meters', b'Meters'), (b'Kilometers', b'Kilometers')], default=b'Meters', max_length=12),
        ),
    ]

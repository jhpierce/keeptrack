# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 16:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0006_normalrun_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=1)),
                ('distance', models.FloatField()),
                ('duration', models.DurationField()),
                ('place', models.PositiveIntegerField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='Meet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='race',
            name='activity',
        ),
        migrations.DeleteModel(
            name='Race',
        ),
        migrations.AddField(
            model_name='event',
            name='meet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log.Meet'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 06:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_auto_20170301_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ship',
            name='captain',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.ShipCaptain'),
        ),
    ]

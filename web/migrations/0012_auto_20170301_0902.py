# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 09:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_person_email_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email_address',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]

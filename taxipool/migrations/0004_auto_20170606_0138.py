# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-05 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxipool', '0003_auto_20170606_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seek_taxi',
            name='num_person',
            field=models.IntegerField(max_length=4),
        ),
    ]

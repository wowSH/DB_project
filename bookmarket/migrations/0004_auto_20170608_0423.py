# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-07 19:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarket', '0003_auto_20170608_0404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid_candidate',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='product_register',
            name='register_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 8, 4, 23, 11, 806367)),
        ),
    ]
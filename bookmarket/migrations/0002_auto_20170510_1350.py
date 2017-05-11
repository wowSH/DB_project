# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(default=datetime.datetime(2017, 5, 10, 4, 50, 29, 798664, tzinfo=utc), max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sel_reg',
            name='s_name',
            field=models.CharField(default=datetime.datetime(2017, 5, 10, 4, 50, 39, 161341, tzinfo=utc), max_length=40),
            preserve_default=False,
        ),
    ]

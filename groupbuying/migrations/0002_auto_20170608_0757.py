# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-07 22:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groupbuying', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party_open',
            name='now_person',
            field=models.IntegerField(default=1),
        ),
    ]

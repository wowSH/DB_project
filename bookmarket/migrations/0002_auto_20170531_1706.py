# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-31 17:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarket', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='c_hp',
            new_name='hp',
        ),
        migrations.RenameField(
            model_name='candidate',
            old_name='c_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='sel_reg',
            old_name='s_hp',
            new_name='hp',
        ),
        migrations.RenameField(
            model_name='sel_reg',
            old_name='s_name',
            new_name='name',
        ),
    ]

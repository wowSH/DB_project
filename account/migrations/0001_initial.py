# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('u_id', models.IntegerField(max_length=8)),
                ('name', models.CharField(max_length=20)),
                ('passward', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('HP', models.IntegerField(max_length=10)),
            ],
        ),
    ]

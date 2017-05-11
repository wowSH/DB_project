# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='HP',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='u_id',
            field=models.IntegerField(),
        ),
    ]

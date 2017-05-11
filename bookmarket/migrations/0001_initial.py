# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('c_id', models.IntegerField()),
                ('bid_date', models.DateTimeField()),
                ('bid_price', models.IntegerField()),
                ('priority', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('c_id', models.IntegerField(default=0)),
                ('c_name', models.CharField(max_length=40)),
                ('c_hp', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('p_id', models.IntegerField(default=0)),
                ('category', models.CharField(max_length=40)),
                ('author', models.CharField(max_length=40)),
                ('subject', models.CharField(max_length=40)),
                ('state', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Sel_Reg',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('s_id', models.IntegerField()),
                ('s_hp', models.CharField(max_length=40)),
                ('register_date', models.DateTimeField()),
                ('init_price', models.IntegerField()),
                ('imm_price', models.IntegerField()),
                ('closing_date', models.DateTimeField()),
                ('p_id', models.ForeignKey(to='bookmarket.Product')),
            ],
        ),
        migrations.AddField(
            model_name='bid',
            name='p_id',
            field=models.ForeignKey(to='bookmarket.Product'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-04 14:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import groupbuying.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('hp', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apply_date', models.DateTimeField()),
                ('comment', models.CharField(max_length=100)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groupbuying.Applicant')),
            ],
        ),
        migrations.CreateModel(
            name='Party_Open',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('category', models.CharField(choices=[('DE', 'Delivery'), ('CO', 'Cosmetic'), ('EL', 'Electronic'), ('ET', 'Etc')], default='ET', max_length=40)),
                ('content', models.CharField(max_length=40)),
                ('open_date', models.DateTimeField()),
                ('num_person', models.IntegerField()),
                ('closing_date', models.DateTimeField()),
                ('image', models.ImageField(default=0, upload_to=groupbuying.models.user_directory_path)),
                ('recruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('hp', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(

            model_name='apply',
            name='party',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groupbuying.Party_Open'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='applying',
            field=models.ManyToManyField(through='groupbuying.Apply', to='groupbuying.Party_Open'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-21 21:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_event_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gov_id', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=500)),
                ('summary', models.CharField(max_length=500)),
                ('url', models.CharField(max_length=500)),
            ],
        ),
    ]

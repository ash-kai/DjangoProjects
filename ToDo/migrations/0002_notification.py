# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-09 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.CharField(default=None, max_length=20)),
            ],
        ),
    ]

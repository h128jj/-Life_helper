# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-29 02:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_auto_20170403_0501'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='desc',
            field=models.CharField(default='', max_length=10000, verbose_name='Description'),
            preserve_default=False,
        ),
    ]

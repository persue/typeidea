# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-11-28 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0003_auto_20191127_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sidebar',
            name='status',
            field=models.PositiveIntegerField(choices=[(1, '展示'), (0, '隐藏')], default=1, verbose_name='状态'),
        ),
    ]

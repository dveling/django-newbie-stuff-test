# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0002_auto_20171202_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='paint_color',
            field=models.CharField(default=None, max_length=128),
        ),
    ]
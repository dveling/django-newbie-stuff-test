# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-05 19:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='f_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='l_name',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='m_intital',
            new_name='middle_intital',
        ),
        migrations.AlterUniqueTogether(
            name='person',
            unique_together=set([('first_name', 'middle_intital', 'last_name', 'date_of_birth', 'SSN')]),
        ),
    ]

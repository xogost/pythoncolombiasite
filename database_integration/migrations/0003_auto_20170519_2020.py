# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-20 01:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database_integration', '0002_auto_20170519_2014'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GroupTypes',
            new_name='GroupType',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 16:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotador', '0005_auto_20170522_1241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='culture',
            old_name='culture_name',
            new_name='name',
        ),
    ]

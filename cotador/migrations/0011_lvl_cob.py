# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotador', '0010_auto_20170523_2055'),
    ]

    operations = [
        migrations.CreateModel(
            name='lvl_cob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 23:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotador', '0009_safra_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tax',
            name='safra',
        ),
        migrations.AddField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]

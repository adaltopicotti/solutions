# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 15:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cotador', '0006_auto_20170522_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prod_Esp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_esp', models.FloatField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cotador.City')),
            ],
        ),
    ]

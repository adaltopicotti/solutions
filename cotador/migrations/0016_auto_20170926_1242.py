# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 15:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cotador', '0015_auto_20170925_1224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Decision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choices', models.ManyToManyField(to='cotador.Choice')),
                ('decision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cotador.Decision')),
            ],
        ),
        migrations.AlterField(
            model_name='quotation',
            name='lvl_cob',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cotador.Lvl_Cob'),
        ),
        migrations.AddField(
            model_name='choice',
            name='decision',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cotador.Decision'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-23 17:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cotador', '0013_auto_20170915_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('protocol', models.CharField(max_length=10)),
                ('area', models.FloatField()),
                ('sack_price', models.FloatField()),
                ('prod_esp', models.FloatField()),
                ('prod_seg', models.FloatField()),
                ('total_is', models.FloatField()),
                ('total_cost', models.FloatField()),
                ('subv_fed', models.FloatField()),
                ('subv_est', models.FloatField()),
                ('final_cost', models.FloatField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cotador.City')),
            ],
        ),
        migrations.AlterField(
            model_name='preregister',
            name='cpf_cnpj',
            field=models.CharField(max_length=14, unique=True),
        ),
        migrations.AddField(
            model_name='quotation',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cotador.PreRegister'),
        ),
        migrations.AddField(
            model_name='quotation',
            name='lvl_cob',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cotador.Lvl_Cob'),
        ),
        migrations.AddField(
            model_name='quotation',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cotador.Product'),
        ),
        migrations.AddField(
            model_name='quotation',
            name='uf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cotador.Uf'),
        ),
    ]

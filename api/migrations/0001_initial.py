# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 16:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=50, null=True)),
                ('price', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=5)),
                ('full_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='pricedata',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Stock'),
        ),
    ]

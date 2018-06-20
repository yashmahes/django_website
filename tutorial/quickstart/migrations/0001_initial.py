# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-06-20 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('sku', models.CharField(max_length=200)),
                ('variant', models.CharField(max_length=200)),
                ('UnitPrice', models.IntegerField()),
                ('SellingPrice', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
                ('location', models.TextField()),
                ('area', models.CharField(max_length=200)),
                ('UnitPrice', models.IntegerField()),
                ('SellingPrice', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('profileimage', models.TextField()),
                ('username', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('mobile', models.IntegerField()),
            ],
        ),
    ]

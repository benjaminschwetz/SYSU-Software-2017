# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-22 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdin', '0021_auto_20171022_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='weightedRelated',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-22 17:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdin', '0018_auto_20171022_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='picture',
            field=models.URLField(max_length=1000, null=True),
        ),
    ]

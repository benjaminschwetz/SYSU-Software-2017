# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-19 01:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdin', '0007_auto_20171019_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='papers',
            name='LogoURL',
            field=models.URLField(max_length=600, null=True),
        ),
    ]

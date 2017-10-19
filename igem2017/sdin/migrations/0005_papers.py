# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-19 01:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdin', '0004_auto_20171019_0111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Papers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DOI', models.CharField(default='', max_length=200, unique=True)),
                ('Title', models.CharField(default='', max_length=100)),
                ('Journal', models.CharField(default='', max_length=150)),
                ('JIF', models.FloatField(default=0)),
                ('ArticleURL', models.URLField()),
                ('LogoURL', models.URLField(null=True)),
                ('Abstract', models.TextField(default='To be add')),
                ('Keywords', models.TextField(default='To be add')),
                ('Authors', models.TextField(default='To be add')),
                ('ReadCount', models.IntegerField(default=0)),
            ],
        ),
    ]

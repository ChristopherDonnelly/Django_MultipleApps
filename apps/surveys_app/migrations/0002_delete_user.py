# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-19 19:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveys_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]

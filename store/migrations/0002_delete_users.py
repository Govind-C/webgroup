# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 14:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-03 17:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbir', '0008_auto_20160203_1639'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='blue',
            new_name='bgrHist',
        ),
        migrations.RemoveField(
            model_name='image',
            name='green',
        ),
        migrations.RemoveField(
            model_name='image',
            name='red',
        ),
    ]

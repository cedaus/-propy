# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-22 11:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_ans'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ans',
            name='question',
        ),
        migrations.DeleteModel(
            name='Ans',
        ),
    ]

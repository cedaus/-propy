# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-20 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='caste',
            field=models.CharField(choices=[(b'Scheduled Castes', b'SC'), (b'General', b'GN'), (b'Other Backward Classes ', b'OBC'), (b'Scheduled Tribes', b'ST')], default='GN', max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='death',
            field=models.DateField(blank=True, null=True),
        ),
    ]
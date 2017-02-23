# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-20 14:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAadhar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('aadhar', models.IntegerField(default=None, max_length=100)),
                ('verified', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-created'],
                'get_latest_by': 'created',
            },
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('address_line_1', models.TextField()),
                ('address_line_2', models.TextField()),
                ('landmark', models.TextField()),
                ('pin_code', models.IntegerField(default=1)),
                ('district', models.CharField(blank=True, max_length=150, null=True)),
                ('state', models.CharField(choices=[(b'Andhra Pradesh', b'AP'), (b'Andaman and Nicobar Islands', b'AN')], max_length=100)),
                ('country', models.CharField(default='INDIA', max_length=50)),
                ('permanent', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserBankDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_account_name', models.CharField(blank=True, max_length=150, null=True)),
                ('bank_account_number', models.TextField(blank=True, null=True)),
                ('bank_ifsc', models.TextField(blank=True, null=True)),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserPhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('phone_number', models.CharField(max_length=100)),
                ('calling_code', models.CharField(default='91', max_length=10)),
                ('verified', models.BooleanField(default=False)),
                ('verification_uid', models.CharField(blank=True, max_length=10, null=True)),
                ('primary', models.BooleanField(default=False)),
                ('last_verified_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-created'],
                'get_latest_by': 'created',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('signup_done', models.BooleanField(default=False)),
                ('signup_stage', models.IntegerField(default=1)),
                ('email_verified', models.BooleanField(default=False)),
                ('authorised', models.BooleanField(default=True)),
                ('blocked', models.BooleanField(default=False)),
                ('gender', models.CharField(choices=[(b'Male', b'M'), (b'Transgender', b'T'), (b'Female', b'F')], max_length=100)),
                ('language', models.CharField(choices=[(b'Hindi', b'HI'), (b'English', b'EN')], max_length=100)),
                ('profession', models.CharField(choices=[(b'Unemployed', b'UNEMPLOYED'), (b'Private Employee', b'PRIVATE EMPLOYEE'), (b'Self Employed', b'SELF EMPLOYED'), (b'Student', b'STUDENT'), (b'Public Employee', b'PUBLIC EMPLOYEE')], max_length=100)),
                ('pan_num', models.CharField(max_length=10, unique=True)),
                ('birth', models.DateField()),
                ('death', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='userphonenumber',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile'),
        ),
        migrations.AddField(
            model_name='userbankdetails',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile'),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile'),
        ),
        migrations.AddField(
            model_name='useraadhar',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile'),
        ),
        migrations.AlterUniqueTogether(
            name='userphonenumber',
            unique_together=set([('user_profile', 'phone_number')]),
        ),
        migrations.AlterUniqueTogether(
            name='useraadhar',
            unique_together=set([('user_profile', 'aadhar')]),
        ),
    ]
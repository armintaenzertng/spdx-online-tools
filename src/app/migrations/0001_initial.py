# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-18 16:17
from __future__ import unicode_literals

import datetime
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
            name='LicenseNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LicenseNamespace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('licenseAuthorName', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('fullname', models.CharField(max_length=70)),
                ('shortIdentifier', models.CharField(max_length=25)),
                ('submissionDatetime', models.DateTimeField(auto_now_add=True)),
                ('userEmail', models.EmailField(max_length=35)),
                ('notes', models.CharField(default='', max_length=255)),
                ('xml', models.TextField()),
                ('archive', models.BooleanField(default=False)),
                ('publiclyShared', models.BooleanField(default=True)),
                ('description', models.TextField()),
                ('namespace', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('license_list_url', models.URLField(max_length=250)),
                ('github_repo_url', models.URLField(max_length=250)),
                ('promoted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'LicenseNamespace',
                'verbose_name_plural': 'LicenseNamespaces',
            },
        ),
        migrations.CreateModel(
            name='LicenseRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('licenseAuthorName', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('fullname', models.CharField(max_length=70)),
                ('shortIdentifier', models.CharField(max_length=25)),
                ('submissionDatetime', models.DateTimeField(auto_now_add=True)),
                ('userEmail', models.EmailField(max_length=35)),
                ('notes', models.CharField(default='', max_length=255)),
                ('xml', models.TextField()),
                ('archive', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'LicenseRequest',
                'verbose_name_plural': 'LicenseRequests',
            },
        ),
        migrations.CreateModel(
            name='OrganisationName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('orgId', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'OrganisationName',
                'verbose_name_plural': 'OrganisationNames',
            },
        ),
        migrations.CreateModel(
            name='UserID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation', models.CharField(max_length=64, verbose_name='Organisation')),
                ('lastlogin', models.DateField(blank=True, default=datetime.datetime.now, verbose_name='Last Login')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='licensenamespace',
            name='license_request',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.LicenseRequest'),
        ),
        migrations.AddField(
            model_name='licensenamespace',
            name='organisation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.OrganisationName'),
        ),
    ]

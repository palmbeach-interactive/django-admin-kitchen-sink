# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-07 21:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchensink', '0008_sink'),
    ]

    operations = [
        migrations.AddField(
            model_name='sink',
            name='subtitle_b',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sink',
            name='title_b',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sink',
            name='subtitle',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sink',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-08 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toolbox', '0016_auto_20161208_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completetoolbox',
            name='datetime_end',
            field=models.DateTimeField(blank=True, help_text='And some words about how to use "this" field.', null=True),
        ),
        migrations.AlterField(
            model_name='completetoolbox',
            name='datetime_start',
            field=models.DateTimeField(blank=True, help_text='And some words about how to use "this" field.', null=True),
        ),
        migrations.AlterField(
            model_name='relationtoolbox',
            name='datetime_end',
            field=models.DateTimeField(blank=True, help_text='And some words about how to use "this" field.', null=True),
        ),
        migrations.AlterField(
            model_name='relationtoolbox',
            name='datetime_start',
            field=models.DateTimeField(blank=True, help_text='And some words about how to use "this" field.', null=True),
        ),
    ]

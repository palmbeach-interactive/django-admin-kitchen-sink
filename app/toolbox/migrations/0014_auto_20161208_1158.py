# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-08 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toolbox', '0013_auto_20161208_1151'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FilerToolbox',
        ),
        migrations.AlterField(
            model_name='toolboxinlineitem',
            name='time_added',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

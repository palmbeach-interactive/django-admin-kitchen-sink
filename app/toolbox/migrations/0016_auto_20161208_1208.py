# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-08 11:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('toolbox', '0015_auto_20161208_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='inlinefilerfile',
            name='toolbox',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='toolbox.InlineToolbox'),
        ),
        migrations.AddField(
            model_name='inlinefilerimage',
            name='toolbox',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='toolbox.InlineToolbox'),
        ),
    ]

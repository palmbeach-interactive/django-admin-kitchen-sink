# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-07 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchensink', '0007_auto_20161207_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='title')),
                ('subtitle', models.CharField(blank=True, max_length=100, null=True, verbose_name='subtitle')),
            ],
            options={
                'verbose_name': 'Sink',
                'verbose_name_plural': 'Sinks',
            },
        ),
    ]

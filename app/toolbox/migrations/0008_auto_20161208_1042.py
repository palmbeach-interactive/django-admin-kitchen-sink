# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-08 09:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('toolbox', '0007_auto_20161208_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='completetoolbox',
            name='long_description',
            field=models.TextField(blank=True, help_text='And some words about how to use "this" field.', null=True),
        ),
        migrations.AlterField(
            model_name='completetoolbox',
            name='date_end',
            field=models.DateField(blank=True, help_text='And some words about how to use "this" field.', null=True),
        ),
        migrations.AlterField(
            model_name='completetoolbox',
            name='date_start',
            field=models.DateField(blank=True, help_text='And some words about how to use "this" field.', null=True),
        ),
        migrations.AlterField(
            model_name='completetoolbox',
            name='datetime_end',
            field=models.DateField(blank=True, help_text='And some words about how to use "this" field.', null=True),
        ),
        migrations.AlterField(
            model_name='completetoolbox',
            name='datetime_start',
            field=models.DateField(blank=True, help_text='And some words about how to use "this" field.', null=True),
        ),
        migrations.AlterField(
            model_name='completetoolbox',
            name='description',
            field=models.CharField(blank=True, help_text='And some words about how to use "this" field.', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='completetoolbox',
            name='name',
            field=models.CharField(help_text='And some words about how to use "this" field.', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='completetoolbox',
            name='tool',
            field=models.ForeignKey(blank=True, help_text='And some words about how to use "this" field.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='toolboxes_fk_a', to='toolbox.SimpleTool'),
        ),
        migrations.AlterField(
            model_name='completetoolbox',
            name='tool_radio_horizontal',
            field=models.ForeignKey(blank=True, help_text='And some words about how to use "this" field.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='toolboxes_fk_d', to='toolbox.SimpleTool2'),
        ),
        migrations.AlterField(
            model_name='completetoolbox',
            name='tool_radio_vertical',
            field=models.ForeignKey(blank=True, help_text='And some words about how to use "this" field.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='toolboxes_fk_c', to='toolbox.SimpleTool2'),
        ),
        migrations.AlterField(
            model_name='completetoolbox',
            name='tool_raw',
            field=models.ForeignKey(blank=True, help_text='And some words about how to use "this" field.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='toolboxes_fk_b', to='toolbox.SimpleTool'),
        ),
        migrations.AlterField(
            model_name='completetoolbox',
            name='tools',
            field=models.ManyToManyField(blank=True, help_text='And some words about how to use "this" field.', related_name='toolboxes', to='toolbox.SimpleTool2'),
        ),
        migrations.AlterField(
            model_name='completetoolbox',
            name='tools_horizontal',
            field=models.ManyToManyField(blank=True, help_text='And some words about how to use "this" field.', related_name='toolboxes_b', to='toolbox.SimpleTool2'),
        ),
        migrations.AlterField(
            model_name='completetoolbox',
            name='tools_through',
            field=models.ManyToManyField(blank=True, help_text='And some words about how to use "this" field.', related_name='toolboxes_f', through='toolbox.ToolboxItem', to='toolbox.SimpleTool'),
        ),
        migrations.AlterField(
            model_name='completetoolbox',
            name='tools_vertical',
            field=models.ManyToManyField(blank=True, help_text='And some words about how to use "this" field.', related_name='toolboxes_c', to='toolbox.SimpleTool2'),
        ),
    ]

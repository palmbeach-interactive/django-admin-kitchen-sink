# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
import random
import string
import uuid

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from filer.fields.folder import FilerFolderField
from hvad.manager import TranslationManager
from easy_thumbnails.files import get_thumbnailer
from hvad.models import TranslatableModel, TranslatedFields
from multiselectfield import MultiSelectField
from django.db.models.signals import post_save
from django.dispatch import receiver




DEMO_HELP_TEXT = 'And some words about how to use "this" field.'


class SimpleTool(models.Model):

    name = models.CharField(
        null=True,
        max_length=100,
    )
    description = models.CharField(
        null=True, blank=True,
        max_length=100,
        help_text='The Subitle'
    )
    date_start = models.DateField(
        null=True, blank=True,
        help_text='The Date'
    )
    date_end = models.DateField(
        null=True, blank=True,
        help_text='The Date (END)'
    )

    class Meta:
        verbose_name = _('Simple Tool')

    def __unicode__(self):
        return self.name




class SimpleTool2(models.Model):

    name = models.CharField(
        null=True,
        max_length=100,
    )
    description = models.CharField(
        null=True, blank=True,
        max_length=100,
        help_text='The Subitle'
    )
    date_start = models.DateField(
        null=True, blank=True,
        help_text='The Date'
    )
    date_end = models.DateField(
        null=True, blank=True,
        help_text='The Date (END)'
    )

    class Meta:
        verbose_name = _('Simple Tool (Inlines)')
        verbose_name_plural = _('Simple Tool (Inlines)')

    def __unicode__(self):
        return self.name


class ToolboxItem(models.Model):

    toolbox = models.ForeignKey('toolbox.RelationToolbox')
    tool = models.ForeignKey('toolbox.SimpleTool')
    time_added = models.DateTimeField(auto_now=True)
    document = models.FileField(null=True, blank=True)


class CompleteToolboxBase(models.Model):


    ###########################################################
    # basic fields
    ###########################################################
    name = models.CharField(
        null=True,
        max_length=100,
        help_text=DEMO_HELP_TEXT
    )
    description = models.CharField(
        null=True, blank=True,
        max_length=100,
        help_text=DEMO_HELP_TEXT
    )
    long_description = models.TextField(
        null=True, blank=True,
        help_text=DEMO_HELP_TEXT
    )

    is_active = models.BooleanField(
        default=False,
        help_text=DEMO_HELP_TEXT
    )

    is_nice = models.NullBooleanField(
        help_text=DEMO_HELP_TEXT
    )

    ###########################################################
    # time / date
    ###########################################################
    date_start = models.DateField(
        null=True, blank=True,
        help_text=DEMO_HELP_TEXT
    )
    date_end = models.DateField(
        null=True, blank=True,
        help_text=DEMO_HELP_TEXT
    )
    datetime_start = models.DateTimeField(
        null=True, blank=True,
        help_text=DEMO_HELP_TEXT
    )
    datetime_end = models.DateTimeField(
        null=True, blank=True,
        help_text=DEMO_HELP_TEXT
    )

    time = models.TimeField(
        null=True, blank=True,
        help_text=DEMO_HELP_TEXT
    )

    duration = models.DurationField(
        null=True, blank=True,
        help_text=DEMO_HELP_TEXT
    )


    ###########################################################
    # files (django)
    ###########################################################
    document = models.FileField(
        null=True, blank=True,
        help_text=DEMO_HELP_TEXT
    )
    image = models.ImageField(
        null=True, blank=True,
        help_text=DEMO_HELP_TEXT
    )



    ###########################################################
    # files (filer)
    ###########################################################
    filer_document = FilerFileField(
        null=True, blank=True,
        related_name='%(app_label)s_%(class)s_filer_a',
        help_text=DEMO_HELP_TEXT
    )
    filer_image = FilerImageField(
        null=True, blank=True,
        related_name='%(app_label)s_%(class)s_filer_b',
        help_text=DEMO_HELP_TEXT
    )
    filer_directory = FilerFolderField(
        null=True, blank=True,
        related_name='%(app_label)s_%(class)s_filer_c',
        help_text=DEMO_HELP_TEXT
    )

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name


class CompleteToolbox(CompleteToolboxBase):

    class Meta:
        verbose_name = _('Complete Toolbox')


class RelationToolbox(CompleteToolboxBase):

    ###########################################################
    # relations
    ###########################################################
    tool = models.ForeignKey(
        SimpleTool, null=True, blank=True, related_name='%(app_label)s_%(class)s_fk_a',
        help_text=DEMO_HELP_TEXT
    )
    tool_raw = models.ForeignKey(
        SimpleTool, null=True, blank=True, related_name='%(app_label)s_%(class)s_fk_b',
        help_text=DEMO_HELP_TEXT
    )

    tool_radio_vertical = models.ForeignKey(
        SimpleTool2, null=True, blank=True, related_name='%(app_label)s_%(class)s_fk_c',
        help_text=DEMO_HELP_TEXT
    )
    tool_radio_horizontal = models.ForeignKey(
        SimpleTool2, null=True, blank=True, related_name='%(app_label)s_%(class)s_fk_d',
        help_text=DEMO_HELP_TEXT
    )

    tools = models.ManyToManyField(
        SimpleTool2, blank=True, related_name='%(app_label)s_%(class)sbox',
        help_text=DEMO_HELP_TEXT
    )
    tools_horizontal = models.ManyToManyField(
        SimpleTool2, blank=True, related_name='%(app_label)s_%(class)s_b',
        help_text=DEMO_HELP_TEXT
    )
    tools_vertical = models.ManyToManyField(
        SimpleTool2, blank=True, related_name='%(app_label)s_%(class)s_c',
        help_text=DEMO_HELP_TEXT
    )
    tools_through = models.ManyToManyField(
        SimpleTool, through='toolbox.ToolboxItem', blank=True, related_name='%(app_label)s_%(class)s_f',
        help_text=DEMO_HELP_TEXT
    )

    class Meta:
        verbose_name = _('Relation Toolbox')




class ToolboxInlineItem(models.Model):

    toolbox = models.ForeignKey('toolbox.InlineToolbox')
    tool = models.ForeignKey(
        'toolbox.SimpleTool',
        help_text=DEMO_HELP_TEXT
    )
    time_added = models.DateTimeField(
        auto_now=False, blank=True, null=True,
        help_text=DEMO_HELP_TEXT
    )
    document = models.FileField(
        null=True, blank=True,
        help_text=DEMO_HELP_TEXT
    )



class InlineFilerImage(models.Model):

    toolbox = models.ForeignKey('toolbox.InlineToolbox', null=True)

    image = FilerImageField(
        help_text=DEMO_HELP_TEXT
    )
    caption = models.CharField(
        max_length=64, null=True,
        help_text=DEMO_HELP_TEXT
    )
    date = models.DateField(
        null=True, blank=True,
        help_text=DEMO_HELP_TEXT
    )

class InlineFilerFile(models.Model):

    toolbox = models.ForeignKey('toolbox.InlineToolbox', null=True)

    file = FilerFileField(
        help_text=DEMO_HELP_TEXT
    )
    filename = models.CharField(
        max_length=64, null=True,
        help_text=DEMO_HELP_TEXT
    )

class InlineToolbox(models.Model):

    tools_through = models.ManyToManyField(
        SimpleTool, through='toolbox.ToolboxInlineItem', blank=True, related_name='%(app_label)s_%(class)s_f',
        help_text=DEMO_HELP_TEXT
    )

    class Meta:
        verbose_name = _('inline Toolbox')


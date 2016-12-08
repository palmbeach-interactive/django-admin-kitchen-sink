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
from hvad.manager import TranslationManager
from easy_thumbnails.files import get_thumbnailer
from hvad.models import TranslatableModel, TranslatedFields
from multiselectfield import MultiSelectField
from django.db.models.signals import post_save
from django.dispatch import receiver


THUMBNAIL_OPT = dict(size=(120, 80), crop=True, bw=False, quality=80)

log = logging.getLogger(__name__)


COLOR_CHOICES = (
    (1, _('red')),
    (2, _('blue')),
)



class Cupboard(TranslatableModel):

    translations = TranslatedFields(
        name=models.CharField(
            verbose_name=_('name'),
            null=True,
            max_length=100,
        ),
        description=models.TextField(
            verbose_name=_('Description'),
            blank=True, null=True,
            max_length=100,
        )
    )

    image = models.ImageField(
        verbose_name=_('picture'),
        blank=True, null=True,
    )

    color = models.IntegerField(
        verbose_name=_('color'),
        choices=COLOR_CHOICES,
        blank=True, null=True
    )

    last_time_cleaned = models.DateTimeField(
        verbose_name=_('last time cleaned'),
        blank=True, null=True,
    )

    class Meta:
        app_label = 'kitchensink'
        verbose_name = _('Cupboard')
        verbose_name_plural = _('Cupboards')

    def __unicode__(self):
        return self.lazy_translation_getter('name', str(self.pk))


class Appliance(models.Model):


    TYPE_CHOICES = (
        ('fridge', _('fridge')),
    )

    type = models.CharField(
        verbose_name=_('type'),
        choices=TYPE_CHOICES,
        null=True, blank=True,
        max_length=32,
    )

    brand = models.CharField(
        verbose_name=_('brand'),
        null=True,
        max_length=100,
    )

    model = models.CharField(
        verbose_name=_('model'),
        null=True, blank=True,
        max_length=100,
    )

    image = models.ImageField(
        verbose_name=_('picture'),
        blank=True, null=True,
    )

    color = models.IntegerField(
        verbose_name=_('color'),
        choices=COLOR_CHOICES,
        blank=True, null=True
    )

    class Meta:
        app_label = 'kitchensink'
        verbose_name = _('Appliance')
        verbose_name_plural = _('Appliances')

    def __unicode__(self):
        if not self.type:
            return self.model

        return '{} ({})'.format(self.model, self.type)



class ApplianceService(models.Model):

    appliance = models.ForeignKey('kitchensink.Appliance')
    date = models.DateField()
    notes = models.CharField(max_length=128)

    class Meta:
        app_label = 'kitchensink'
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    def __unicode__(self):

        return '{} ({})'.format(self.appliance, self.date)



class Sink(models.Model):

    title = models.CharField(
        null=True,
        max_length=100,
        help_text='The Title'
    )
    subtitle = models.CharField(
        null=True, blank=True,
        max_length=100,
        help_text='The Subitle'
    )
    date_start = models.DateField(
        null=True, blank=True,
        help_text='The Date'
    )
    datetime_start = models.DateTimeField(
        null=True, blank=True,
        help_text='The Datetime'
    )
    date_end = models.DateField(
        null=True, blank=True,
        help_text='The Date (END)'
    )
    datetime_end = models.DateTimeField(
        null=True, blank=True,
        help_text='The Datetime (END)'
    )


    class Meta:
        app_label = 'kitchensink'
        verbose_name = _('Sink')
        verbose_name_plural = _('Sinks')

    def __unicode__(self):
        return self.title


class SinkBit(models.Model):

    sink = models.ForeignKey('kitchensink.Sink')

    title = models.CharField(
        null=True,
        max_length=100,
        help_text='The Title'
    )
    subtitle = models.CharField(
        null=True, blank=True,
        max_length=100,
        help_text='The Subitle'
    )
    date_start = models.DateField(
        null=True, blank=True,
        help_text='The Date'
    )
    datetime_start = models.DateTimeField(
        null=True, blank=True,
        help_text='The Datetime'
    )
    date_end = models.DateField(
        null=True, blank=True,
        help_text='The Date (END)'
    )
    datetime_end = models.DateTimeField(
        null=True, blank=True,
        help_text='The Datetime (END)'
    )


    class Meta:
        app_label = 'kitchensink'
        verbose_name = _('Sink Bit')
        verbose_name_plural = _('Sink Bits')

    def __unicode__(self):
        return self.title


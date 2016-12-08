# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.contrib import messages
from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.template.defaultfilters import truncatechars
from django.core import urlresolvers
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.files import get_thumbnailer
from hvad.admin import TranslatableAdmin, TranslatableTabularInline
from charsleft_widget.widgets import CharsLeftCharFieldWidget, CharsLeftTextFieldWidget


THUMBNAIL_OPT = dict(size=(120, 80), crop=True, bw=False, quality=80)

from .models import (SimpleTool, SimpleTool2, CompleteToolbox, RelationToolbox, InlineToolbox,
                     ToolboxInlineItem, InlineFilerImage, InlineFilerFile)



@admin.register(SimpleTool)
class SimpleToolAdmin(admin.ModelAdmin):
    save_on_top = True


@admin.register(SimpleTool2)
class SimpleTool2Admin(admin.ModelAdmin):
    save_on_top = True



@admin.register(CompleteToolbox)
class CompleteToolboxAdmin(admin.ModelAdmin):
    save_on_top = True

    fieldsets = (

        ###########################################################
        # basic fields
        ###########################################################
        (None, {
            'fields': (
                'name',
                'description',
                'long_description',
                'is_active',
                'is_nice',
            )
        }),
        ('Basic Fields (aligned)', {
            'description': 'The basic fields - multi column',
            #'classes': ('wide',),
            'fields': (
                ('name', 'description',),
                ('is_active', 'is_nice',),
                'long_description',
            ),
        }),
        ('Basic Fields (wide)', {
            'description': 'The basic fields - "wide" style',
            'classes': ('wide',),
            'fields': (
                ('name', 'description',),
                'long_description',
                ('is_nice', 'is_active',),
            ),
        }),
        ('Basic Fields (wide & collapsed)', {
            'description': 'The basic fields - "wide" style with a long long long description, even <br>The linebreaks here...',
            'classes': ('wide', 'collapse'),
            'fields': (
                'long_description',
                ('is_active', 'is_nice',),
                ('name', 'description',),
            ),
        }),

        ###########################################################
        # time / date
        ###########################################################
        ('Dates & Times', {
            'fields': (
                'name',
                'date_start',
                'date_end',
                'datetime_start',
                'datetime_end',
                'time',
                'duration',
                'is_active',
            ),
        }),
        ('Dates & Times (aligned)', {
            'description': 'Dates & Times - multi column',
            'fields': (
                'name',
                ('date_start', 'date_end',),
                ('datetime_start', 'datetime_end',),
                ('time', 'duration',),
            ),
        }),
        ('Dates & Times (aligned)', {
            'description': 'Dates & Times - 3 column',
            'fields': (
                'name',
                ('date_start', 'time', 'date_end',),
                ('duration', 'datetime_start', 'datetime_end',),
            ),
        }),
        ('Dates & Times (wide)', {
            'description': 'Dates & Times - "wide" style',
            'classes': ('wide',),
            'fields': (
                ('datetime_end', 'date_end',),
                ('datetime_start', 'date_start',),
                ('duration', 'time',),
                'name',
            ),
        }),
        ('Dates & Times (wide & collapsed)', {
            'description': 'Dates & Times - collapsed',
            'classes': ('wide', 'collapse'),
            'fields': (
                ('datetime_end', 'date_end',),
                ('datetime_start', 'date_start',),
                ('long_description', 'duration',),
                ('name', 'time',),
            ),
        }),

        ###########################################################
        # files / images / filer
        ###########################################################
        ('Files, Images & Filer', {
            'fields': (
                'document',
                'image',
                'filer_document',
                'filer_image',
                'filer_directory',
            ),
        }),
        ('Files, Images & Filer (aligned)', {
            'fields': (
                ('document', 'image',),
                'filer_directory',
                ('filer_document', 'filer_image',),
                ('name', 'time',),
            ),
        }),
        ('Files, Images & Filer (collapsed)', {
            'classes': ('collapse',),
            'fields': (
                ('is_active', 'is_nice',),
                ('document', 'image',),
                'filer_directory',
                ('filer_document', 'filer_image',),
                ('name', 'time',),
            ),
        }),

    )




@admin.register(RelationToolbox)
class RelationToolboxAdmin(admin.ModelAdmin):
    save_on_top = True

    raw_id_fields = [
        'tool_raw',
    ]

    filter_horizontal = [
        'tools_horizontal',
    ]

    filter_vertical = [
        'tools_vertical',
    ]

    radio_fields = {
        'tool_radio_vertical': admin.VERTICAL,
        'tool_radio_horizontal': admin.HORIZONTAL,
    }

    fieldsets = (
        ###########################################################
        # basic relation display
        ###########################################################
        (None, {
            'fields': (
                'tool',
                'tool_raw',
                'tool_radio_vertical',
                'tool_radio_horizontal',
                'tools',
                'tools_horizontal',
                'tools_vertical',
                #'tools_through',
            )
        }),
        ('Relations (wide)', {
            'classes': ('wide',),
            'fields': (
                'tool',
                'tool_raw',
                'tool_radio_vertical',
                'tool_radio_horizontal',
                'tools',
                'tools_horizontal',
                'tools_vertical',
            ),
        }),
        ('Relations (wide)', {
            'classes': ('collapse',),
            'fields': (
                'tool',
                'tool_raw',
                ('tool_radio_vertical', 'tool_radio_horizontal',),
                'tools',
                'tools_horizontal',
                'tools_vertical',
            ),
        }),
    )


class ToolboxInlineItemInline(admin.TabularInline):
    model = ToolboxInlineItem
    extra = 2



class ToolboxInlineItemStacked(admin.StackedInline):
    model = ToolboxInlineItem
    extra = 2

    fieldsets = (
        ###########################################################
        # basic relation display
        ###########################################################
        (None, {

            'description': 'Some morfe shizzle here',
            'fields': (
                'time_added',
                'document',
                'tool',
            )
        }),
        ('Additional Info', {
            'description': 'Some morfe shizzle here',
            'classes': ('collapse',),
            'fields': (
                ('tool'),
                ('time_added', 'document',),
            ),
        }),
    )



class FilerImageInline(admin.TabularInline):
    model = InlineFilerImage



class FilerFileInline(admin.TabularInline):
    model = InlineFilerFile




@admin.register(InlineToolbox)
class InlineToolboxAdmin(admin.ModelAdmin):
    save_on_top = True

    inlines = [
        ToolboxInlineItemInline,
        ToolboxInlineItemStacked,
        FilerImageInline,
        FilerFileInline,
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.contrib import messages
from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.template.defaultfilters import truncatechars
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from parler.admin import TranslatableAdmin, TranslatableTabularInline


THUMBNAIL_OPT = dict(size=(120, 80), crop=True, bw=False, quality=80)

from .models import Cupboard, Appliance, ApplianceService, Sink, SinkBit



class ImageAdminMixin(admin.ModelAdmin):

    def key_image(self, obj):

        if obj.image:
            try:
                return u'<img src="%s" />' % (get_thumbnailer(obj.image).get_thumbnail(THUMBNAIL_OPT).url)
            except Exception as e:
                return '{} {}'.format(_('Unable to process image'), e)
        else:
            return '{}'.format(_('No image'))

    key_image.short_description = _('Image')
    key_image.allow_tags = True


@admin.register(Cupboard)
class CupboardAdmin(TranslatableAdmin):
    save_on_top = True

    date_hierarchy = 'last_time_cleaned'

    search_fields = [
        'translations__name',
        'translations__description',
    ]

    list_filter = [
        'last_time_cleaned',
        'color',
    ]

    list_display = [
        'cupboard_info',
        'color',
        'cleaned_this_month',
    ]

    def cupboard_info(self, obj):

        tpl = u"""<p>
            <strong><a href="{admin_url}">{title}</a></strong><br>
            <hr>
            <p>{description}</p>
            </p>""".format(
            admin_url=reverse('admin:kitchensink_cupboard_change', args=(obj.pk,)),
            title=obj.name,
            description=truncatechars(obj.description, 30) if obj.description else '-',
        )

        return tpl

    cupboard_info.short_description = _('Cupboard')
    cupboard_info.allow_tags = True


    def cleaned_this_month(self, obj):
        if not obj.last_time_cleaned:
            return False
        return obj.last_time_cleaned > (timezone.now() - timedelta(days=31))

    cleaned_this_month.short_description = _('Cleaned this month')
    cleaned_this_month.allow_tags = True
    cleaned_this_month.boolean = True



class ApplianceServiceInline(admin.TabularInline):
    model = ApplianceService
    extra = 0


@admin.register(Appliance)
class ApplianceAdmin(admin.ModelAdmin):
    save_on_top = True

    inlines = [
        ApplianceServiceInline,
    ]


class SinkBitTabularInline(admin.TabularInline):
    model = SinkBit
    extra = 1



class SinkBitStackedInline(admin.StackedInline):
    model = SinkBit
    extra = 1




@admin.register(Sink)
class SinkAdmin(admin.ModelAdmin):
    save_on_top = True


    fieldsets = (
        (None, {
            'fields': (
                ('title', 'subtitle',),
                'date_start',
                'datetime_start',
                ('date_end', 'datetime_end',),
            )
        }),
    )

    inlines = [
        SinkBitTabularInline,
        SinkBitStackedInline,
    ]

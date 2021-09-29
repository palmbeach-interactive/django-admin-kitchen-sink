# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from admin_tools.dashboard import modules, Dashboard, AppIndexDashboard
from admin_tools.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for website.
    """
    columns = 2

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        request = context['request']

        self.children.append(modules.LinkList(
            _('Quick links'),
            layout='inline',
            draggable=False,
            deletable=False,
            collapsible=False,
            #children=children,
            children=[
                {
                    'title': _('Appliances'),
                    'url': reverse('admin:kitchensink_appliance_changelist'),
                    #'url': '#',
                    'css_classes': 'build',
                    'disabled': not request.user.has_perm('kitchensink.change_appliance'),
                },
                {
                    'title': _('Clients'),
                    #'url': reverse('admin:pop_client_changelist'),
                    'url': '#',
                    'css_classes': 'devices_other',
                    'disabled': not request.user.has_perm('pop.change_client'),
                },
                {
                    'title': _('Locations'),
                    #'url': reverse('admin:pop_location_changelist'),
                    'url': '#',
                    'css_classes': 'location_on',
                    'disabled': not request.user.has_perm('pop.change_location'),
                },
                {
                    'title': _('Regions'),
                    #'url': reverse('admin:pop_region_changelist'),
                    'url': '#',
                    'css_classes': 'terrain',
                    'disabled': not request.user.has_perm('pop.change_region'),
                },

                {
                    'title': _('Countries'),
                    #'url': reverse('admin:pop_country_changelist'),
                    'url': '#',
                    'css_classes': 'flag',
                    'disabled': not request.user.has_perm('pop.change_country'),
                },
                {
                    'title': _('Dateien & Ordner'),
                    #'url': reverse('admin:filer_folder_changelist'),
                    'url': '#',
                    'external': False,
                    'css_classes': 'folder_special',
                    'disabled': not request.user.has_perm('filer.change_file'),
                },
                {
                    'title': _('Users'),
                    #'url': reverse('admin:cas_profile_user_changelist'),
                    'url': '#',
                    'external': False,
                    'css_classes': 'person_pin',
                    'disabled': not request.user.has_perm('cas_profile.change_user'),
                },
                {
                    'title': _('Groups'),
                    #'url': reverse('admin:auth_group_changelist'),
                    'url': '#',
                    'external': False,
                    'css_classes': 'group',
                    'disabled': not request.user.has_perm('auth.change_group'),
                },
            ],
            show_title=False,
            template='admin_tools/dashboard/modules/quicklist_panel.html',
            css_classes=['quicklinks',],
            pre_content=_('Kitchen Sink - Dashboard')
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Letzte Aktionen'),
            css_classes=['recent-actions'],
            template='admin_tools/dashboard/modules/recent_actions.html',
            limit=5,
            deletable=False,
        ))

        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Support & Tickets'),
            layout='inline',
            draggable=False,
            deletable=False,
            collapsible=False,
            show_title=False,
            children=[
                {
                    'title': _('Bug melden'),
                    'url': 'https://lab.hazelfire.com/projects/swissmusic-ch/issues/new',
                    'external': True,
                    'css_classes': 'bug_report',
                },
                {
                    'title': _('Bug melden (E-Mail)'),
                    'url': 'mailto:lab@hazelfire.com?body=%0D%0A%0D%0AProject: swissmusic-ch',
                    'external': True,
                    'css_classes': 'send',
                },
                {
                    'title': _('Dokumentation'),
                    'url': 'https://swissmusic.ch/doc/',
                    'external': True,
                    'css_classes': 'lightbulb_outline',
                },
            ],
            template='admin_tools/dashboard/modules/quicklist_panel.html',
            css_classes=['quicklinks', 'support-panel', 'no-postit-header'],
            pre_content=_('Swiss Music - App Übersicht')
        ))

        # append an app list module for "Applications"
        '''
        self.children.append(modules.AppList(
            _('CMS Administration'),
            deletable=False,
            models=('cms.*', 'filer.*', 'cmsplugin_filer_image.*',),
        ))
        '''

        # append an app list module for "Applications"
        self.children.append(modules.AppList(
            _('Custom Apps'),
            deletable=False,
            exclude=('django.contrib.*', 'user_extra.*', 'cms.*', 'cmsplugin_filer_image.*', 'dummy.*', 'filer.*',),
        ))

        # append an app list module for "Administration"
        self.children.append(modules.AppList(
            _('Users & Groups'),
            deletable=False,
            models=('django.contrib.*', 'user_extra.*',),
        ))



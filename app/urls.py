from django.urls import include, path, re_path
from django.conf.urls.i18n import i18n_patterns, set_language

# from solid_i18n.urls import solid_i18n_patterns
from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.views.static import serve
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

SITE_URL = getattr(settings, "SITE_URL")

admin.autodiscover()
admin.site.site_header = "Django Admin Kitchen Sink - {}".format(SITE_URL)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("cms.urls")),
]


if settings.DEBUG:
    urlpatterns += [
        re_path(
            r"^media/(?P<path>.*)$",
            serve,
            {
                "document_root": settings.MEDIA_ROOT,
            },
        ),
    ]

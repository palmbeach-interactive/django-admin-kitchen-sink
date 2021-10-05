# -*- coding: utf-8 -*-
import logging

from django.conf import settings

DEVSERVER_HEADER = "HTTP_" + getattr(
    settings, "WEBPACK_DEVSERVER_HEADER", "X-WEBPACK-DEVSERVER"
).replace("-", "_")

logger = logging.getLogger(__name__)


class WebpackDevserverMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.META.get(DEVSERVER_HEADER, False):
            request.webpack_devserver = True

        response = self.get_response(request)
        return response

import json

import os
from django.contrib.staticfiles.storage import staticfiles_storage
from django.template import Library

from django.conf import settings

register = Library()


def static(path):
    return staticfiles_storage.url(path)


@register.simple_tag
def assets(*args):
    if settings.DEBUG:
        try:
            with open(settings.WEBPACK_ASSET_JSON) as assetfile:
                assets_ = json.load(assetfile)
                for arg in args:
                    if assets_:
                        assets_ = assets_.get(arg)
                    else:
                        return ''

                if assets_:
                    return static(assets_)
                else:
                    return ''
        except:
            return ''
    else:
        try:
            assets_ = settings.WEBPACK_ASSETS

            for arg in args:
                if assets_:
                    assets_ = assets_.get(arg)
                else:
                    return ''

            if assets_:
                return static(assets_)
            else:
                return ''
        except:
            return ''

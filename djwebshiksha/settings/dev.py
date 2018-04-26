from .base import *

SECRET_KEY = 'sm@g)(fbwdh5wc*xe@j++m9rh^uza5se9a57c5ptwkg*b@ki0x'

DEBUG = True
"""
Martor static files are not working in  DEBUG = True
In DEBUG = False, media is served by server (i.e. nginx, apache)

"""
# ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "..", "static"),
)
STATIC_ROOT = os.path.join(BASE_DIR, "live-static-files", "static-root")
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "live-static-files", "media-root")

INSTALLED_APPS += (
    'debug_toolbar',
)
AUTH_PASSWORD_VALIDATORS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '..', 'db.sqlite3'),
    }
}
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

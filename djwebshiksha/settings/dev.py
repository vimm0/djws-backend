from .base import *

SECRET_KEY = 'sm@g)(fbwdh5wc*xe@j++m9rh^uza5se9a57c5ptwkg*b@ki0x'

DEBUG = True

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '..', 'static'),
)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "..", "..", "static")
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "..", "..", "media")

INSTALLED_APPS += (
    'debug_toolbar',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '..', 'db.sqlite3'),
    }
}
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

AUTH_PASSWORD_VALIDATORS = []

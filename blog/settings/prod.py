from .base import *

SECRET_KEY = 'sm@g)(fbwdh5wc*xe@j++m9rh^uza5se9a57c5ptwkg*b@ki0x'

DEBUG = True

ALLOWED_HOSTS = []

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
STATIC_ROOT = os.path.join(BASE_DIR, "live-static-files", "static-root")
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "live-static-files", "media-root")

# STATIC_ROOT = os.path.join(BASE_DIR, '..', '..', 'static')
# STATIC_URL = '/static/'
# MEDIA_ROOT = os.path.join(BASE_DIR, '..', '..', 'media')
# MEDIA_URL = '/media/'

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


INTERNAL_IPS = '127.0.0.1'
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'edusanjal',
#         'USER': 'postgres',
#         'PASSWORD': 'password',
#         'HOST': '',
#         'PORT': '',
#         'ATOMIC_REQUESTS': True,
#     }
# }

AUTH_PASSWORD_VALIDATORS = []



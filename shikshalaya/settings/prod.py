import dj_database_url
from dj_database_url import config

from .base import *

DEBUG = os.environ.get('DEBUG', True)
# SECRET_KEY = 'sm@g)(fbwdh5wc*xe@j++m9rh^uza5se9a57c5ptwkg*b@ki0x'
ALLOWED_HOSTS = ['https://shikshalaya.herokuapp.com/', 'localhost']

# SECRET_KEY = config('SECRET_KEY')
# DEBUG = config('DEBUG', default=True)
SECRET_KEY = os.environ.get('SECRET_KEY', 'sm@g)(fbwdh5wc*xe@j++m9rh^uza5se9a57c5ptwkg*b@ki0x')

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
STATIC_ROOT = os.path.join(BASE_DIR, "live-static-files", "static-root")
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "live-static-files", "media-root")

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, '..', 'db.sqlite3'),
#     }
# }
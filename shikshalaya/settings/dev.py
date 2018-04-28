from .base import *

import dj_database_url
# from dj_database_url import config

SECRET_KEY = os.environ.get('SECRET_KEY', 'sm@g)(fbwdh5wc*xe@j++m9rh^uza5se9a57c5ptwkg*b@ki0x')

# SECRET_KEY = config('SECRET_KEY')
# DEBUG = config('DEBUG', default=True, cast=bool)
# DATABASES = {
#     'default': dj_database_url.config(
#         default=config('DATABASE_URL')
#     )
# }
DEBUG = True
db_from_env = dj_database_url.config()
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, '..', 'db.sqlite3'),
    # }
}
DATABASES['default'].update(db_from_env)
# DATABASES['default']['CONN_MAX_AGE'] = 500
ALLOWED_HOSTS = ['https://shikshalaya.herokuapp.com/', 'localhost']
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

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

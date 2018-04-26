# """MY BASE VERSION"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INTERNAL_IPS = ['127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # flat pages
    'django.contrib.sites',
    'django.contrib.flatpages',
    # third party
    'crispy_forms',
    'markdown_deux',
    'pagedown',
    # 'analytical',
    # 'ckeditor',
    'taggit',
    'rest_framework',
    'corsheaders',

    # local apps
    'apps.accounts',
    'apps.comments',
    'apps.posts',
    'apps.web_sikhshalaya',
]

SITE_ID = 1
CRISPY_TEMPLATE_PACK = 'bootstrap3'

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # flat pages
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

# MIDDLEWARE = [
#     # ...
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
#     # ...
# ]
#

LOGIN_URL = "/login/"
ROOT_URLCONF = 'djwebshiksha.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djwebshiksha.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [{'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
                            {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
                            {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
                            {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
                            ]

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "..", "static"),
)

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'vimmrana0@gmail.com'
EMAIL_HOST_PASSWORD = '9815510732'
EMAIL_PORT = 587

FROALA_INCLUDE_JQUERY = False

# Redactor settings
REDACTOR_OPTIONS = {'lang': 'en'}
REDACTOR_UPLOAD = 'uploads/'

CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    'localhost:8000',
    '127.0.0.1:8000'
)

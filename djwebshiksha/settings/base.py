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
    'whitenoise.runserver_nostatic',
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
    'markdownx',

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

##################### MARKDOWN EDITOR ##########################

# # Global martor settings
# # Input: string boolean, `true/false`
# MARTOR_ENABLE_CONFIGS = {
#     'imgur': 'true',     # to enable/disable imgur/custom uploader.
#     'mention': 'false',  # to enable/disable mention
#     'jquery': 'true',    # to include/revoke jquery (require for admin default django)
# }
#
# # To setup the martor editor with label or not (default is False)
# MARTOR_ENABLE_LABEL = False
#
# # Imgur API Keys
# MARTOR_IMGUR_CLIENT_ID = 'your-client-id'
# MARTOR_IMGUR_API_KEY   = 'your-api-key'
#
# # Safe Mode
# MARTOR_MARKDOWN_SAFE_MODE = True # default
#
# # Markdownify
# MARTOR_MARKDOWNIFY_FUNCTION = 'martor.utils.markdownify' # default
# MARTOR_MARKDOWNIFY_URL = '/martor/markdownify/' # default
#
# # Markdown extensions (default)
# MARTOR_MARKDOWN_EXTENSIONS = [
#     'markdown.extensions.extra',
#     'markdown.extensions.nl2br',
#     'markdown.extensions.smarty',
#     'markdown.extensions.fenced_code',
#
#     # Custom markdown extensions.
#     'martor.extensions.urlize',
#     'martor.extensions.del_ins', # ~~strikethrough~~ and ++underscores++
#     'martor.extensions.mention', # require for mention
#     'martor.extensions.emoji',   # require for emoji
# ]
#
# # Markdown Extensions Configs
# MARTOR_MARKDOWN_EXTENSION_CONFIGS = {}
#
# # Markdown urls
# MARTOR_UPLOAD_URL = '/martor/uploader/' # default
# MARTOR_SEARCH_USERS_URL = '/martor/search-user/' # default
#
# # Markdown Extensions
# MARTOR_MARKDOWN_BASE_EMOJI_URL = 'https://assets-cdn.github.com/images/icons/emoji/' # default
# MARTOR_MARKDOWN_BASE_MENTION_URL = 'https://python.web.id/author/' # default (change this)
#
# CSRF_COOKIE_HTTPONLY = False

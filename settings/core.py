# Copyright 2022 ITCase (info@itcase.pro)

# Main settings for project

from . import BASE_DIR
from .project import PROJECT_NAME

# A list of all the people who get code error notifications
ADMINS = [('ITCase', 'error@itcase.pro')]
# A list in the same format as ADMINS that specifies who should get broken link
# notifications when BrokenLinkEmailsMiddleware is enabled.
MANAGERS = ADMINS

# This is used to provide cryptographic signing, and should be set to a unique,
# unpredictable value.
SECRET_KEY = 'django-insecure-fxxkmli&wu&sajpl6&q^l1fd5ne1q-vb*w54(a68(_i6npya$3'

# A list of strings designating all applications that are enabled.
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    # third-party
    'django_rq',
    'filebrowser',
    'grappelli.dashboard',
    'grappelli',
    'rest_framework',
    'rest_framework.authtoken',

    # should be last for overridings
    'django.contrib.admin',
]

# A list of middleware to use
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

# A string representing the full Python import path to your root URLconf.
ROOT_URLCONF = 'urls'

# A list containing the settings for all template engines.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.joinpath('templates')],
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


# A dictionary containing the settings for all databases to be used.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': '127.0.0.1',
        'NAME': PROJECT_NAME,
        'PORT': 5432,
        'USER': PROJECT_NAME,
    }
}

# Default primary key field type
# https://docs.djangoproject.com/en/dev/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': ('django.contrib.auth.password_validation'
                 '.UserAttributeSimilarityValidator'),
    },
    {
        'NAME': ('django.contrib.auth.password_validation'
                 '.MinimumLengthValidator'),
    },
    {
        'NAME': ('django.contrib.auth.password_validation'
                 '.CommonPasswordValidator'),
    },
    {
        'NAME': ('django.contrib.auth.password_validation'
                 '.NumericPasswordValidator'),
    },
]

# Managing static files
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/
STATICFILES_DIRS = []
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
STATIC_ROOT = BASE_DIR / 'static'
STATIC_URL = f'/{STATIC_ROOT.stem}/'

# Managing upload files
# https://docs.djangoproject.com/en/dev/topics/files/
FILE_UPLOAD_PERMISSIONS = 0o644
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = f'/{MEDIA_ROOT.stem}/'

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/
# A string representing the language code for this installation.
LANGUAGE_CODE = 'ru-ru'
# A boolean that specifies if datetimes will be timezone-aware by default.
USE_TZ = True
TIME_ZONE = 'Asia/Yekaterinburg'
# A boolean that specifies whether Django’s translation system will be enabled.
USE_I18N = True
# A boolean that specifies if localized formatting of data will be enabled.
USE_L10N = True
THOUSAND_SEPARATOR = ' '
USE_THOUSAND_SEPARATOR = True

# Controls where Django stores session data.
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
# If you’re using cache-based session storage, this selects the cache to use.
SESSION_CACHE_ALIAS = 'session'

# The ID, as an integer, of the current site in the django_site database table.
SITE_ID = 1

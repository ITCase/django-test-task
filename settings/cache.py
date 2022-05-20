# Copyright 2022 ITCase (info@itcase.pro)

# Django Redis
# https://github.com/jazzband/django-redis

from .project import PROJECT_NAME

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/0',
        'TIMEOUT': 60 * 60 * 2,
        'KEY_PREFIX': PROJECT_NAME,
        'OPTIONS': {
            'IGNORE_EXCEPTIONS': True,
        }
    },
    'session': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'KEY_PREFIX': PROJECT_NAME,
    },
    'queue': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/2',
        'KEY_PREFIX': PROJECT_NAME,
        'OPTIONS': {
            'IGNORE_EXCEPTIONS': True,
        }
    },
}

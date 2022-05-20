# Copyright 2022 ITCase (info@itcase.pro)

from copy import deepcopy

from django.utils.log import DEFAULT_LOGGING

LOGGING = deepcopy(DEFAULT_LOGGING)

# ****************************************************************
# DJANGO

if 'formatters' not in LOGGING:
    LOGGING['formatters'] = {}

LOGGING['formatters'].update({
    'simple': {
        'format': '%(levelname)s %(asctime)s %(message)s'
    },
    'verbose': {
        'format': ('%(levelname)s %(asctime)s - %(pathname)s - L %(lineno)d'
                   '\n\t%(message)s')
    },
})

if 'handlers' not in LOGGING:
    LOGGING['handlers'] = {}

# Handler for disabled loggers
LOGGING['handlers']['null'] = {'class': 'logging.NullHandler'}

# Allow catch 40x HTTP errors
LOGGING['handlers']['mail_admins']['level'] = 'CRITICAL'

# Disable any supposed filters
try:
    del LOGGING['handlers']['console']['filters']
except KeyError:
    pass

LOGGING['handlers']['console']['formatter'] = 'simple'

if 'loggers' not in LOGGING:
    LOGGING['loggers'] = {}

# Disable 'Invalid HTTP_HOST' errors
LOGGING['loggers']['django.security.DisallowedHost'] = {
    'handlers': ['null'],
    'propagate': False,
}

# ****************************************************************
# PROJECT

_format = LOGGING['formatters']['verbose']['format']

# Uses for custom management commands
LOGGING['formatters']['management'] = {'format': 'MANAGEMENT ' + _format}
LOGGING['handlers']['management'] = {
    'class': 'logging.StreamHandler',
    'formatter': 'management',
    'level': 'DEBUG',
}
LOGGING['loggers']['management'] = {
    'handlers': ['management'],
    'level': 'WARNING',
}

# ****************************************************************
# ITCASE

# from itcase_plugin import logging as itcase_plugin_logging  # noqa

# LOGGING['formatters'].update(itcase_plugin_logging.FORMATTERS)
# LOGGING['handlers'].update(itcase_plugin_logging.HANDLERS)
# LOGGING['loggers'].update(itcase_plugin_logging.LOGGERS)

# ****************************************************************
# THIRD-PARTY

# Django RQ
# https://github.com/rq/django-rq
LOGGING['handlers']['rq_console'] = {
    'class': 'rq.utils.ColorizingStreamHandler',
    'exclude': ('%(levelname)s', '%(asctime)s'),
    'filters': ['require_debug_true'],
    'formatter': 'simple',
    'level': 'DEBUG',
}
LOGGING['loggers']['rq.worker'] = {
    'handlers': ['rq_console'],
    'level': 'WARNING'
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'style': '{',
    'formatters': {
        'TiLeMe': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        },
        'TiLeMePa': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s'
        },
        'TiLeMePaIn': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname) %(exc_info)s'
        },
        'TiLeMeMo': {
            'format': '%(asctime)s %(levelname)s %(message)s %(module)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'debugs': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'TiLeMe',
            'filters': ['require_debug_true']
        },
        'warnings': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'TiLeMePa',
            'filters': ['require_debug_true']
        },
        'errors': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'TiLeMePaIn',
            'filters': ['require_debug_true']
        },
        'general': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'general.log',
            'formatter': 'TiLeMeMo',
            'filters': ['require_debug_false']
        },
        'errors_file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'errors.log',
            'formatter': 'TiLeMePaIn'
        },
        'security': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'security.log',
            'formatter': 'TiLeMeMo'
        },
        'to_mail': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'TiLeMePa',
            'filters': ['require_debug_false']
        }
    },
    'loggers': {
        'django': {
            'handlers': ['debugs', 'warnings', 'errors', 'general'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['errors_file', 'to_mail'],
            'propagate': False,
        },
        'django.server': {
            'handlers': ['errors_file', 'to_mail'],
            'propagate': False,
        },
        'django.template': {
            'handlers': ['errors_file'],
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['errors_file'],
            'propagate': False,
        },
        'django.security': {
            'handlers': ['security'],
            'propagate': False,
        },
    }
}

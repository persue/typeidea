# -*- coding: utf-8 -*-
from .base import *  # NOQA

DEBUG = False

#ALLOWED_HOSTS=['robin.com']

REDIS_URL='127.0.0.1:6379:1'

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'typeidea_db',
        'USER':'root',
        'PASSWORD':'wu123456',
        'HOST':'127.0.0.1',
        'PORT':3306,
        'CONN_MAX_AGE':60,
        'OPTIONS':{'charset':'utf8mb4'},
    }
}

ADMINS=MANAGERS=(
    ('robin','robin@admin.com'),
)

STATIC_ROOT = '/home/robin/py36env/static_files/'

LOGGING = {
    'version':1,
    'disable_existing_loggers':False,
    'formatters':{
        'default': {
            'format': '%(levelname)s %(asctime)s %(module)s:'
                      '%(funcName)s:%(lineno)d %(message)s'
        },
    },
    'handlers':{
        'console':{
            'level':'INFO',
            'class':'logging.StreamHandler',
            'formatter':'default',
        },

    	'file':{
        	'level':'INFO',
        	'class':'logging.handlers.RotatingFileHandler',
        	'filename':'/tmp/logs/typeidea.log',
        	'formatter':'default',
        	'maxBytes':1024*1024,
        	'backupCount':5,
    	},
	},
    'loggers':{
        '':{
            'handlers':['console'],
            'level':'INFO',
            'propagate':True,
        },
    }
}
'''
CACHES = {
    'default':{
        'ENGINE': 'django_redis.cache.RedisCache',
        'LOCATION':REDIS_URL,
        'TIMEOUT':300,
        'OPTIONS':{
            #'PASSWORD':'wu123456',
            'CLIENT_CLASS':'django_redis.client.DefaultClient',
            'PARSER_CLASS':'redis.connection.HiredisParser',
            },
        'CONNECTION_POOL_CLASS':'redis.connection.BlockingConnectionPool',
    }
}
'''
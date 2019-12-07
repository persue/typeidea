from .base import *  # NOQA

DEBUG = False

ALLOWED_HOSTS=['robin.com']

REDIS_URL='127.0.0.1:6379:1'

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'typeidea_db',
        'USER':'root',
        'PASSWORD':'wu123456',
        'HOST':'127.0.0.1',
        'PORT':3306,
        #'CONN_MAx_AGE':5*60,
        'OPTIONS':{'charset':'utf8mb4'},
    }
}


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
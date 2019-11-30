from .base import *  # NOQA

DEBUG = False

ALLOWED_HOSTS=['robin.com']

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
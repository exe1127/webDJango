from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # Conector de DB
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'moni',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

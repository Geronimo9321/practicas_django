from .base import *

DEBUG = True

SECRET_KEY = 'django-insecure-tf0rc)@ku1pm)22dj!uyrr2*3%yq&d90f_$%li=8di2337v3%7'

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
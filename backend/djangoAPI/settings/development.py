import os
from .common import *


###############
# ENVIRONMENT #
###############

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j530&6(ni7@++i_h!uw)p%-x$#))1nvbtq&n&xp3sj)_2k52v!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

def show_toolbar(request):
    """
    The default callback checks if the IP is internal, but docker's IP
    addresses are not in INTERNAL_IPS, so we force the display in dev mode
    :param request: The intercepted request
    :return: True
    """
    return True

DEV_APPS = [
    'debug_toolbar',
    'corsheaders',
]

INSTALLED_APPS = INSTALLED_APPS + DEV_APPS

DEV_MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

MIDDLEWARE = MIDDLEWARE + DEV_MIDDLEWARE  # CORS middleware should be at the top of the list

CORS_ORIGIN_ALLOW_ALL = True

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar,
    'SKIP_TEMPLATE_PREFIXES': (
        'django/forms/widgets/',
        'admin/widgets/',
        'menus/',
        'pipeline/',
    ),
}

############
# DATANASE #
############

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'daniel',
        'PASSWORD': 'daniel',
        'HOST': 'database',
        'PORT': '5432',
    }
}


###########
# STATICS #
###########

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


##########
# CELERY #
##########

# Broker settings.
CELERY_BROKER_USE_SSL = False
CELERY_BROKER_URL = ''
CELERY_TIMEZONE = TIME_ZONE

# Task result backend
CELERY_RESULT_BACKEND = 'amqp'

# AMQP backend settings
CELERY_RESULT_SERIALIZER = 'json'
CELERY_RESULT_EXPIRES = 3600

# Task execution
CELERY_TASK_IGNORE_RESULT = True
CELERY_WORKER_DISABLE_RATE_LIMITS = True

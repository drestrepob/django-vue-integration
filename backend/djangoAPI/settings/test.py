import os
from .common import *


###############
# ENVIRONMENT #
###############

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9^qu(43w608c9@t$n1&-!kck^rt##9zw$m7x)a%aw^scd3au!1'


# Database for CI/CD github actions

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("POSTGRES_DB"),
        'USER': os.environ.get("POSTGRES_USER"),
        'PASSWORD': os.environ.get("POSTGRES_PASSWORD"),
        'HOST': '127.0.0.1',
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

CELERY_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPOGATES=True

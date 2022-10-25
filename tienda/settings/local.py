<<<<<<< HEAD
#from msilib.schema import Media
=======
>>>>>>> a3abf924def9d4760f6c57c892ee8f40fac00216
from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado',
        'USER': 'pedro',
        'PASSWORD': 'root1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

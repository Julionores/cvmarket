from . import *

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'djaure-hotm7*piwyvt10jnts6_zro@gaso&--*r@*!*uewuj@k+!f-)q'
DEBUG = False
ALLOWED_HOSTS = ['localhost','127.0.0.1','cvmarket.herokuapp.com','192.168.211.130']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cvmarket',
        'USER': 'julionores',
        'PASSWORD': 'toor',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

#
# Google Drive Storage Settings
#
GOOGLE_DRIVE_STORAGE_JSON_KEY_FILE = os.path.join(BASE_DIR, 'cvmarketstorage-87a2b946f27b.json')
GOOGLE_DRIVE_STORAGE_MEDIA_ROOT = 'media/' # OPTIONAL


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#db_from_env = dj_database_url.config(conn_max_age=500)
#DATABASES['default'].update(db_from_env)    




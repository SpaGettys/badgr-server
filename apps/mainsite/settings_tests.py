# encoding: utf-8


from cryptography.fernet import Fernet

from .settings import *

# disable logging for tests
LOGGING = {}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'badgr_server',
#         'OPTIONS': {
#             "init_command": "SET default_storage_engine=InnoDB",
#         },
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#        'NAME': os.path.join(TOP_DIR, 'local.sqlite3'),                      # Or path to database file if using sqlite3.
        'NAME': 'badgr',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'root',                  # Not used with sqlite3.
        'HOST': 'mysql_host',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
        'OPTIONS': {
#            "SET character_set_connection=utf8mb3, collation_connection=utf8_unicode_ci",  # Uncomment when using MySQL to ensure consistency across servers
        },
    }
}

CELERY_ALWAYS_EAGER = True
SECRET_KEY = 'aninsecurekeyusedfortesting'
UNSUBSCRIBE_SECRET_KEY = str(SECRET_KEY)
PAGINATION_SECRET_KEY = Fernet.generate_key()
AUTHCODE_SECRET_KEY = Fernet.generate_key()

# Postgres installed locally via http://www.enterprisedb.com/products-services-training/pgdownload#osx

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'tristano',									# Or path to database file if using sqlite3.
        'USER': 'you',
        'PASSWORD': 'your_db_base',
        'HOST': 'localhost',								# Need to specify localhost to override OS X default
        'PORT': '',											# Set to empty string for default.
    }
}

# Print emails to console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Override compressor settings
COMPRESS_OFFLINE = False


# django-allauth stores these in the db - optionally copy here for reference
SOCIAL_AUTH_TWITTER_KEY = 'foo'
SOCIAL_AUTH_TWITTER_SECRET = 'bar'
# FACEBOOK_APP_ID              = 'something'
# FACEBOOK_API_SECRET          = 'else'
# GOOGLE_CONSUMER_KEY          = ''
# GOOGLE_CONSUMER_SECRET       = ''
# GOOGLE_OAUTH2_CLIENT_ID      = ''
# GOOGLE_OAUTH2_CLIENT_SECRET  = ''

# localhost
SITE_ID = 2

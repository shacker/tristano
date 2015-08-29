import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

ADMINS = (
    ('Scot Hacker', 'shacker@birdhouse.org'),
)

MANAGERS = ADMINS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'dbname',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

LOGIN_REDIRECT_URL = '/'

APPEND_SLASH = True

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''


# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(PROJECT_PATH,'static_resources')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = ( os.path.join(PROJECT_PATH,'static/'),)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)


# For django-compressor. True in production only; override in local settings
# Available settings at http://django-compressor.readthedocs.org/en/latest/settings/#settings
# Use `./manage.py compress` to see how production compiles collected assets
COMPRESS_OFFLINE = True  # Override locally
COMPRESS_ENABLED = True
COMPRESS_DATA_URI_MAX_SIZE = 2048
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.datauri.CssDataUriFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]


# Make this unique, and don't share it with anybody.
SECRET_KEY = '99a(0)wfw(&k3_1a-e*f#ycjnf!*)2w^i*xr!b)4b&re+)yx1l'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'allauth.account.context_processors.account',
    'allauth.socialaccount.context_processors.socialaccount',
    'django.contrib.messages.context_processors.messages',
 )

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

ROOT_URLCONF = 'project.urls'


# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'project.wsgi.application'

TEMPLATE_DIRS = (
    PROJECT_PATH + '/templates/allauth',
    PROJECT_PATH + '/templates/',
)

INSTALLED_APPS = (
    # Django apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',

    # 3rd party apps
    'django_extensions',
    'markdown_deux',
    'compressor',
    'rest_framework',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.twitter',

    # Our apps
    'profiles',
    'sampledata',
)

# DJANGO-ALLAUTH OPTIONS
# http://django-allauth.readthedocs.org/en/latest/#configuration
SOCIALACCOUNT_PROVIDERS =  {
    'facebook':
        { 'SCOPE': ['email',],
          'METHOD': 'oauth2'
        },

    'google':
        {   'SCOPE': ['https://www.googleapis.com/auth/userinfo.profile'],
            'AUTH_PARAMS': { 'access_type': 'online' }
        },
    'twitter': {},

}

# This callable sets the profile display_name, which in turn supports the allauth template tag: {% user_display user %}
# ACCOUNT_USER_DISPLAY = "cir.profiles.models.get_or_set_display_name"
ACCOUNT_AUTHENTICATION_METHOD = ("email")
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
# ACCOUNT_SIGNUP_FORM_CLASS = 'profiles.forms.RegistrationForm'  # Use this to add additional fields on signup
# ACCOUNT_PASSWORD_MIN_LENGTH = 8  # Not needed with social logins only
# Attempt to bypass the signup form by using fields (e.g. username, email) retrieved from the social account provider.
# Works for Twitter and FB, not for Google.
SOCIALACCOUNT_AUTO_SIGNUP = True


REST_FRAMEWORK = {
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',

    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAdminUser',
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ],

    'PAGINATE_BY': 10
}

# Override CSS class for the ERROR tag level to match Bootstrap class name
from django.contrib.messages import constants as message_constants
MESSAGE_TAGS = {message_constants.ERROR: 'danger'}


#####################################################################
# Default settings go above this line.
# This allows local settings to override.
#####################################################################
from project.local_settings import *
# try:
#     from local_settings import *
# except ImportError:
#     pass

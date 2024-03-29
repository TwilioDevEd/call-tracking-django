"""
Common Django settings for the project.

See the local, test, and production settings modules for the values used
in each environment.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
from django.core.exceptions import ImproperlyConfigured

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'not-so-secret'

ALLOWED_HOSTS = []

# TwimL Application SID - used to give all our phone numbers the same
# voice URL setting. Learn more: https://www.twilio.com/blog/2011/06/introducing-twilio-applications-an-easier-way-to-manage-phone-numbers.html
TWIML_APPLICATION_SID = os.environ.get('TWIML_APPLICATION_SID', None)
if not TWIML_APPLICATION_SID:
    missing_application_sid_message = \
    """
    You *must* set a TWIML_APPLICATION_SID environment variable to run this app.

    Create a TwiML Application here: https://www.twilio.com/user/account/apps/add and set the Voice request URL to this value:

    http://{{ your ngrok/server hostname here }}/call-tracking/forward-call
    """
    raise ImproperlyConfigured(missing_application_sid_message)

TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID', None)
if not TWILIO_ACCOUNT_SID:
    missing_account_sid_message = \
    """
    You *must* set a TWILIO_ACCOUNT_SID environment variable to run this app.
    """
    raise ImproperlyConfigured(missing_account_sid_message)

TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN', None)
if not TWILIO_AUTH_TOKEN:
    missing_auth_token_message = \
    """
    You *must* set a TWILIO_AUTH_TOKEN environment variable to run this app.
    """
    raise ImproperlyConfigured(missing_auth_token_message)

# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize'
)

THIRD_PARTY_APPS = (
    'bootstrap3',
    'django_forms_bootstrap'
)

LOCAL_APPS = (
    'call_tracking',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
)

ROOT_URLCONF = 'twilio_sample_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'twilio_sample_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'call_tracking'
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = BASE_DIR + '/staticfiles'

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Messages settings for Bootstrap 3

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

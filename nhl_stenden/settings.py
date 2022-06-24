from pathlib import Path

import os, sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))
# Import user credentials from db_credentials file
from .db_credentials import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-64*by=^a@tdy0g1rk**k^)&m!#p*dp24(nndo1kp8t9eet2$z('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['10.110.110.117']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main.apps.MainConfig',
    'robot.apps.RobotConfig',
    'users.apps.UsersConfig',
    'methods.apps.MethodsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'nhl_stenden.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_ROOT, 'templates/')],
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

WSGI_APPLICATION = 'nhl_stenden.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}

# Database

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    #'NAME': 'a0643156_nhl_stenden',
    #'USER': 'a0643156_nhl_stenden',
    #'PASSWORD': 'TQ9tUnNA',
    #'HOST': 'mirondiamond.ru',
    'NAME':     db_credentials.DB_NAME,  # change this to your database name (inside db_credentials.py)
    'USER':     db_credentials.DB_USER,  # change this to your username (inside db_credentials.py)
    'PASSWORD': db_credentials.DB_PASS,  # change this to your password (inside db_credentials.py)
    'HOST':     db_credentials.DB_HOST,  # Or an IP Address that your DB is hosted on (inside db_credentials.py)
    'PORT':     db_credentials.DB_PORT,  # change this port to your DB port (inside db_credentials.py)
    'OPTIONS': {
      'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
      'charset': 'utf8mb4',
    }
  }
}


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_ROOT = os.path.join(str(BASE_DIR) + '/nhl_stenden/static/root')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(str(BASE_DIR) + "/nhl_stenden/static/styles"),
)

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

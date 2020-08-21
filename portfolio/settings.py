"""
Django settings for portfolio project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# from portfolio.secret_settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "test" or os.environ.get(
    "SECRET_KEY") or b"\x1c=\xb2\xfa?\xbcn\x91K\x9c\xe7=\x8c\xa5i\xff"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["django-brennan.herokuapp.com", "localhost", "127.0.0.1"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'jobs',
    'storages'
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

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'portfolio.wsgi.application'

# AWS S3 Configuration
# URLs MUST follow this template: 
# https://BUCKETNAME.s3.REGIONNAME.amazonaws.com/folder/file

AWS_STORAGE_BUCKET_NAME = "django-portfolio-brennan" or os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = "us-west-2" or os.environ.get("AWS_S3_REGION_NAME")
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

# Tell django-storages the domain to use to refer to static files.
AWS_S3_CUSTOM_DOMAIN = '%s.s3.%s.amazonaws.com' % (AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME)
AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}
AWS_DEFAULT_ACL = None

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'portfolio.settings.StaticStorage'

MEDIAFILES_LOCATION = 'media'
DEAFULT_FILE_STORAGE = 'portfolio.settings.MediaStorage'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("ENV_NAME") or 'portfoliodb',
        'USER': os.environ.get("ENV_USER") or 'postgres',
        'PASSWORD': os.environ.get("ENV_PASSWORD") or 'password123456',
        'HOST': os.environ.get("ENV_HOST") or 'localhost',
        'PORT': os.environ.get("ENV_PORT") or '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

MEDIA_URL = '/media/'
MEDIA_ROOT = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)


if (os.environ.get("ENV_NAME") != None):
    # Activate Django-Heroku:
    django_heroku.settings(locals())

    import dj_database_url
    DATABASES['default'] = dj_database_url.config(
        conn_max_age=600, ssl_require=True)

from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION

class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION

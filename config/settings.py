"""
Django settings for be_cleys project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
import sys
from pathlib import Path

import django
from dj_database_url import parse as parse_database_url
from django.core.management.utils import get_random_secret_key
from django.utils.translation import gettext_lazy
from dotenv import load_dotenv

django.utils.translation.ugettext_lazy = gettext_lazy

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'False') == 'True'
DEVELOPMENT = True

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '127.0.0.1,localhost,www.localhost').split(',')
INTERNAL_IPS = ["127.0.0.1"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3rd party,
    'imagekit',
    'ckeditor',
    'django_filters',
    'admin_reorder',
    'snowpenguin.django.recaptcha3',
    # local
    'apps.website',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'admin_reorder.middleware.ModelAdminReorder',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.website.context_processors.meta',
                'apps.website.context_processors.contacts',
                'apps.website.context_processors.footer',
                'apps.website.context_processors.reviews',
                'apps.website.context_processors.category_pages',
                'apps.website.context_processors.calculator',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


if DEVELOPMENT:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
elif len(sys.argv) > 0 and sys.argv[1] != 'collectstatic':
    if os.getenv('DATABASE_URL', None) is None:
        raise Exception('DATABASE_URL environment variable not defined')
    DATABASES = {
        'default': parse_database_url(os.environ.get('DATABASE_URL'), conn_max_age=600)
    }

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATICFILES_DIRS = (BASE_DIR.joinpath('config/static'),)
if DEVELOPMENT:
    STATIC_URL = '/static/'
    STATIC_ROOT = BASE_DIR / 'static'
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'media'
else:
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_ENDPOINT_URL = os.getenv('AWS_S3_ENDPOINT_URL')
    AWS_S3_CUSTOM_DOMAIN = os.getenv('AWS_S3_CUSTOM_DOMAIN')
    AWS_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400'
    }
    AWS_DEFAULT_ACL = 'public-read'
    AWS_QUERYSTRING_AUTH = False
    STATICFILES_STORAGE = 'config.custom_storages.StaticStorage'
    DEFAULT_FILE_STORAGE = 'config.custom_storages.MediaStorage'
    STATIC_URL = 'https://{}/static/'.format(
        AWS_S3_CUSTOM_DOMAIN,
    )
    MEDIA_URL = 'https://{}/media/'.format(
        AWS_S3_CUSTOM_DOMAIN,
    )


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# admin reorder settings
# https://pypi.org/project/django-modeladmin-reorder/

ADMIN_REORDER = (
    'auth',
    'sites',
    {'app': 'website',
     'label': 'Base Website Settings',
     'models': (
         {'model': 'website.MetadataModel', 'label': 'Meta Data'},
         {'model': 'website.ContactModel', 'label': 'Contacts'},
         {'model': 'website.FooterModel', 'label': 'Footer'},
         {'model': 'website.ReviewsStarsModel', 'label': 'Review'},
         {'model': 'website.AppointmentModel', 'label': 'Appointment'},
     )
     },
    {'app': 'website',
     'label': 'Base Pages',
     'models': (
         {'model': 'website.AboutUsPageModel', 'label': 'About Us Page'},
         {'model': 'website.ContactPageModel', 'label': 'Contacts Page'},
         {'model': 'website.MakeAppointmentPageModel', 'label': 'Make Appointment Page'},
         {'model': 'website.PremiumLoansPageModel', 'label': 'Premium Loans Page'},
         {'model': 'website.CalculatedBlockModel', 'label': 'Calculator Page'},
         {'model': 'website.AllProjectPageModel', 'label': 'All Project Page'},
         {'model': 'website.IndexPageModel', 'label': 'Home Page'},
         {'model': 'website.PrivacyPolicyModel', 'label': 'Privacy Policy Page'},
         {'model': 'website.CookieModel', 'label': 'Cookies Page'},
         {'model': 'website.TermsAndConditionsModel', 'label': 'Terms And Conditions Page'},
     )
     },
    {'app': 'website',
     'label': 'Category Pages',
     'models': (
         {'model': 'website.CategoryPage', 'label': 'Category Page'},
         {'model': 'website.SingleProjectModel', 'label': 'Single Page'},
     )
     },
    {'app': 'website',
     'label': 'Feedbacks',
     'models': (
         {'model': 'website.Feedback', 'label': 'About Us Feedback'},
         {'model': 'website.ContactFeedbackModel', 'label': 'Contacts Feedback'},
         {'model': 'website.ServicesAppointment', 'label': 'Check Boxes Appointment'},
     )
     },

)

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'height': 400,
        'width': 1024,
        'toolbar_Custom': [
            ['Format', 'RemoveFormat'],
            ['Bold', 'Italic', 'Underline', 'Strike', 'Cite'],
            ['TextColor', 'BGColor'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent'],
            ['Link', 'Unlink', 'Anchor'],
            ['Table', 'HorizontalRule'],
            ['Smiley', 'SpecialChar'],
            ['Undo', 'Redo'],
            ['Source'],
        ],
        'format_tags': 'p;h2;h3;h4;h5;h6',
    },
    'upload': {
        'toolbar': 'Custom',
        'height': 900,
        'width': 1024,
        'toolbar_Custom': [
            ['Format', 'RemoveFormat'],
            ['Bold', 'Italic', 'Underline', 'Strike', 'Cite'],
            ['TextColor', 'BGColor'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Iframe', 'Table', 'HorizontalRule'],
            ['Smiley', 'SpecialChar'],
            ['Undo', 'Redo'],
            ['Source'],
        ],
        'extraPlugins': ['iframe', 'autoembed'],
        'extraAllowedContent': ['iframe[*]', 'video[*]'],
        'format_tags': 'p;h2;h3;h4;h5;h6',
    },
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' if DEBUG else \
    'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = os.getenv('SENDGRID_API_KEY')
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
DEFAULT_TO_EMAIL = os.getenv('DEFAULT_TO_EMAIL')

RECAPTCHA_DISABLE = os.getenv('RECAPTCHA_DISABLE', True)
RECAPTCHA_PRIVATE_KEY = os.getenv('RECAPTCHA_PRIVATE_KEY')
RECAPTCHA_PUBLIC_KEY = os.getenv('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_DEFAULT_ACTION = 'generic'
RECAPTCHA_SCORE_THRESHOLD = 0.5

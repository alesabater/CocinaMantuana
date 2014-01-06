"""
Django settings for PaginaWeb Web/project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$yd!g@qnoi!k%ncw()v4d1^12ja049)x5z(zh-1bx)q3t-)rdq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ADMINS = (
    ('Alejandro Sabater', 'ale.sabaterc@gmail.com'),
    ('Mariana Sabater', 'mariana.sabater@gmail.com'),
)

MANAGERS = (
    ('Alejandro Sabater', 'ale.sabaterc@gmail.com'),
    ('Mariana Sabater', 'mariana.sabater@gmail.com'),
)

SEND_BROKEN_LINK_EMAILS = True

EMAIL_SUBJECT_PREFIX = '[CocinaMantuana Website]'

ALLOWED_HOSTS = []

MEDIA_ROOT = 'PaginaWeb/Web/static'
MEDIA_URL = '/media/'
STATIC_ROOT = '/Web/static'
STATIC_URL = '/Web/static/'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ale.sabaterc@gmail.com'
EMAIL_HOST_PASSWORD = 'a21014106s'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

STATICFILES_DIRS = (

    os.path.join(PROJECT_PATH, 'Web/static'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

ROOT_URLCONF = 'PaginaWeb.Web.urls'

STATICFILES_FINDERS = (

    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'Web/templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'PaginaWeb.Web',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'PaginaWeb.urls'

WSGI_APPLICATION = 'PaginaWeb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'CocinaMantuana',
        'USER': 'root',
        'PASSWORD':'',

    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
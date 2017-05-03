"""
Django settings for application project.

"""

import os

import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Security

DEBUG = True

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

if DEBUG:
    ALLOWED_HOSTS = ['webtrack']
else:
    ALLOWED_HOSTS = ['track-mail-web-kosolapov.herokuapp.com']

    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'bootstrap3',
    'cloudinary',
    'crispy_forms',
    'fm',
    'core.apps.CoreConfig',
    'blogs.apps.BlogsConfig',
    'comments.apps.CommentsConfig',
]

AUTH_USER_MODEL = 'core.User'
LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'core:login'

CRISPY_TEMPLATE_PACK = 'bootstrap3'
DEFAULT_FORM_TEMPLATE = 'fm/form.html'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'application.urls'

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

WSGI_APPLICATION = 'application.wsgi.application'

# Database

db_from_env = dj_database_url.config(conn_max_age=600,
                                     engine='django.db.backends.postgresql_psycopg2')
DATABASES = {
    'default': db_from_env
}

# Logger settings
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%{levelname}s] %{asctime}s %{module}s %{process}d %{thread}d %{message}s'
        },
        'simple': {
            'format': '[%{levelname}s] %{message}s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.environ.get('LOG_FILE', default=os.path.join(BASE_DIR, '../logs/debug.log')),
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'web_track.custom': {
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO'
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

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

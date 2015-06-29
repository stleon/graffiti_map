import os
from django.core.exceptions import ImproperlyConfigured

def get_env_setting(var):
     try:
          return os.environ[var]
     except KeyError:
          raise ImproperlyConfigured('Переменная %s не задана' % var)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROJECT_NAME = 'Graffiti_Map'

SECRET_KEY = get_env_setting('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1',]

INTERNAL_IPS = ('127.0.0.1',)

ADMINS = (
     ('stleon', 'leonst998@gmail.com'),
)

MANAGERS = ADMINS

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'graffities',
    'captcha',
    'rest_framework',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'graffiti_map.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'graffiti_map.wsgi.application'

# Database

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            #'CONN_MAX_AGE': ''
            'NAME': get_env_setting('DB_NAME'),
            'USER': get_env_setting('DB_USER'),
            'PASSWORD': get_env_setting('DB_PASSWORD'),
            'HOST': get_env_setting('DB_HOST'),
            'PORT': get_env_setting('DB_PORT'),
        }
    }

# Internationalization

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Files

STATIC_URL = '/core/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/datastore/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'dynamic')

FILE_UPLOAD_MAX_MEMORY_SIZE = 2621440

# Cookies

CSRF_COOKIE_NAME = 'graffiti_map'

SESSION_COOKIE_SECURE = not DEBUG

CSRF_COOKIE_SECURE = not DEBUG

SESSION_COOKIE_NAME = 'session_graffiti_map'

SESSION_COOKIE_HTTPONLY = True

CSRF_COOKIE_HTTPONLY = True

# ?

X_FRAME_OPTIONS = 'DENY'

FIRST_DAY_OF_WEEK = 1

#CSRF_FAILURE_VIEW

# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Google ReCaptcha

RECAPTCHA_PUBLIC_KEY = get_env_setting('RECAPTCHA_PUBLIC_KEY')

RECAPTCHA_PRIVATE_KEY = get_env_setting('RECAPTCHA_PRIVATE_KEY')

NOCAPTCHA = True

REST_FRAMEWORK = {

    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),

    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),

    'DEFAULT_THROTTLE_RATES': {
        'anon': '10/minute',
        'user': '10/minute'
    },
}

# TODO https://docs.djangoproject.com/en/dev/topics/cache/#setting-up-the-cache

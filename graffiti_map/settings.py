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

DEBUG = False

DOMEN = 'map.partizaning.org'

ALLOWED_HOSTS = ['127.0.0.1', get_env_setting('SERVER_IP'), DOMEN]

INTERNAL_IPS = ('127.0.0.1', )

ADMINS = (('stleon', 'leonst998@gmail.com'), )

MANAGERS = (('Igor', 'iponosov@gmail.com'),
            ('Make', 'makemakemakemake@gmail.com'), )

# Application definition

INSTALLED_APPS = ('django.contrib.admin',
                  'django.contrib.auth',
                  'django.contrib.contenttypes',
                  'django.contrib.sessions',
                  'django.contrib.messages',
                  'django.contrib.staticfiles',
                  'django.contrib.sitemaps',
                  'graffities',
                  'captcha',
                  'rest_framework',
                  'djrill',
                  'sorl.thumbnail',
                  'corsheaders',
                  'django_cleanup', )

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware', )

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

STATIC_ROOT = os.path.join(BASE_DIR, 'collect_static')

MEDIA_URL = '/datastore/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'dynamic')

FILE_UPLOAD_MAX_MEMORY_SIZE = 2621440

# Cookies

CSRF_COOKIE_NAME = 'graffiti_map'

#SESSION_COOKIE_SECURE = not DEBUG

#CSRF_COOKIE_SECURE = not DEBUG

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
            'filters': [
                'require_debug_false'
            ],
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
    'DEFAULT_RENDERER_CLASSES': ('rest_framework.renderers.JSONRenderer', ),
    'DEFAULT_THROTTLE_CLASSES': ('rest_framework.throttling.AnonRateThrottle',
                                 'rest_framework.throttling.UserRateThrottle'),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '10/minute',
        'user': '10/minute'
    },
}

# Mailing

MANDRILL_API_KEY = get_env_setting('MANDRILL_API_KEY')
EMAIL_BACKEND = 'djrill.mail.backends.djrill.DjrillBackend'
EMAIL_HOST_USER = 'partizaning.org@gmail.com'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER  # корреспонденция для менеджеров
SERVER_EMAIL = EMAIL_HOST_USER  # для отправки сообщений о ошибках

ADMIN_URL = get_env_setting('ADMIN_URL')

# TODO https://docs.djangoproject.com/en/dev/topics/cache/#setting-up-the-cache

# CORS

CORS_ORIGIN_ALLOW_ALL = True
CORS_URLS_REGEX = r'^/api/.*$'
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ('x-requested-with',
                      'content-type',
                      'accept',
                      'origin',
                      'authorization',
                      'x-csrftoken',
                      'dnt',
                      'accept-encoding', )

# THUMBNAIL

THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.redis_kvstore.KVStore'
THUMBNAIL_REDIS_HOST = get_env_setting('THUMBNAIL_REDIS_HOST')
THUMBNAIL_REDIS_PORT = get_env_setting('THUMBNAIL_REDIS_PORT')
THUMBNAIL_REDIS_DB = get_env_setting('THUMBNAIL_REDIS_DB')
THUMBNAIL_REDIS_PASSWORD = get_env_setting('THUMBNAIL_REDIS_PASSWORD')
DJANGORESIZED_DEFAULT_KEEP_META = False

# Sessions

SESSION_ENGINE = 'redis_sessions.session'
SESSION_REDIS_HOST = get_env_setting('SESSION_REDIS_HOST')
SESSION_REDIS_PORT = get_env_setting('SESSION_REDIS_PORT')
SESSION_REDIS_DB = get_env_setting('SESSION_REDIS_DB')
SESSION_REDIS_PASSWORD = get_env_setting('SESSION_REDIS_PASSWORD')
SESSION_REDIS_PREFIX = get_env_setting('SESSION_REDIS_PREFIX')

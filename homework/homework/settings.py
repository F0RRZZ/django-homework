import os
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    ALLOWED_HOSTS=(list, ['*']),
    USERS_AUTOACTIVATE=(bool, False),
    DEBUG=(bool, True),
    EMAIL=(str, 'example@example.com'),
    RUSSIAN_WORDS_REVERSING_MIDDLEWARE_ENABLED=(bool, False),
    SECRET_KEY=(str, 'dummy-key'),
)

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

ALLOWED_HOSTS = env('ALLOWED_HOSTS')
DEBUG = env('DEBUG')
EMAIL = env('EMAIL')
RUSSIAN_WORDS_REVERSING_MIDDLEWARE_ENABLED = env(
    'RUSSIAN_WORDS_REVERSING_MIDDLEWARE_ENABLED'
)
SECRET_KEY = env('SECRET_KEY')

MAX_FAILED_ATTEMPTS = 3
USERS_AUTOACTIVATE = True if DEBUG else env('USERS_AUTOACTIVATE')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # installed apps
    'ckeditor',
    'debug_toolbar',
    'django_cleanup.apps.CleanupConfig',
    'sorl.thumbnail',
    # created apps
    'about.apps.AboutConfig',
    'catalog.apps.CatalogConfig',
    'core.apps.CoreConfig',
    'feedback.apps.FeedbackConfig',
    'homepage.apps.HomepageConfig',
    'rating.apps.RatingConfig',
    'statistic.apps.StatisticConfig',
    'users.apps.UsersConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'homework.middleware.custom_middleware.RussianWordsReverseMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1',
]

ROOT_URLCONF = 'homework.urls'

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
                'django.template.context_processors.media',
                'users.context_processors.birthday_users',
            ],
        },
    },
]

WSGI_APPLICATION = 'homework.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.'
        'password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.'
        'password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.'
        'password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.'
        'password_validation.NumericPasswordValidator',
    },
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache'),
    }
}

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static_dev',
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = BASE_DIR / 'sent_emails'

LOGIN_URL = '/auth/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

AUTH_USER_MODEL = 'users.UserProfile'
AUTHENTICATION_BACKENDS = [
    'users.backend.NormalizedEmailAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
]

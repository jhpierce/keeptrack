import os
import json

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'components')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5zi!5%3qifz7re2j4$edi)rj5_hcpaoim9j3g6887($8zv@+r+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []

# Might have to unlock gmail captcha
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = json.loads(open(os.path.expanduser('~')+'/.credentials/email_credentials.json', 'rb+').read())['email_username']+'@gmail.com'
EMAIL_HOST_PASSWORD = json.loads(open(os.path.expanduser('~')+'/.credentials/email_credentials.json', 'rb+').read())['email_password']
EMAIL_PORT = 587
EMAIL_USE_TLS = True

TWILIO_ACCOUNT_SID = json.loads(open(os.path.expanduser('~')+'/.credentials/email_credentials.json', 'rb+').read())['twilio_account_sid']
TWILIO_AUTH_TOKEN = json.loads(open(os.path.expanduser('~')+'/.credentials/email_credentials.json', 'rb+').read())['twilio_auth_token']

LOGIN_URL = '/log/login/'
INVITATIONS_SIGNUP_REDIRECT = 'athlete_signup'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'log.apps.LogConfig',
    'allauth',
    'invitations',
    'widget_tweaks',
    'axes',
    'captcha',
    'django_twilio'
]

ACCOUNT_ADAPTER = 'invitations.models.InvitationsAdapter'

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'keeptrack.urls'

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


WSGI_APPLICATION = 'keeptrack.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'ktdb',
        # 'USER': 'root',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

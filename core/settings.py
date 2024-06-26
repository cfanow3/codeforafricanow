
from pathlib import Path
import os
import json
from google.oauth2 import service_account


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ej16)up%h=2%^=hn90zv+m%%i&-dh%wgzl77x=sd$)l3+pyy%5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "codeforafricanow-xc7m.onrender.com"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #my apps
    'cfa',
    "whitenoise.runserver_nostatic",
    'gdstorage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'core.urls'

DATA_UPLOAD_MAX_MEMORY_SIZE = 52428800  # 50 MB or higher
FILE_UPLOAD_MAX_MEMORY_SIZE = 52428800  # 50 MB or higher

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
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

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 
MEDIA_URL ='/media/'

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static_root')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'cfa.User'


# Check if running in Render.com environment
if os.environ['GOOGLE_APPLICATION_CREDENTIALS_JSON']:
    # Get the JSON content from the environment variable
    credentials_info = json.loads(os.environ['GOOGLE_APPLICATION_CREDENTIALS_JSON'])

    # Define a path for the temporary credentials file
    temp_credentials_path = os.path.join(BASE_DIR, 'credentials.json')

    # Write the JSON content to the temporary file
    with open(temp_credentials_path, 'w') as temp_credentials_file:
        json.dump(credentials_info, temp_credentials_file)

    # Load credentials from the temporary file
    credentials = service_account.Credentials.from_service_account_file(temp_credentials_path)

    # Clean up the temporary file if desired
    os.remove(temp_credentials_path)
else:
    # Load your service account credentials locally
    with open(os.path.join(BASE_DIR, 'cfacredentials.json')) as f:
        credentials_info = json.load(f)

    credentials = service_account.Credentials.from_service_account_info(credentials_info)

GOOGLE_DRIVE_STORAGE_JSON_KEY_FILE = os.path.join(BASE_DIR, 'cfacredentials.json')
DEFAULT_FILE_STORAGE = 'django_googledrive_storage.GoogleDriveStorage'
GS_BUCKET_NAME = 'media'
GS_CREDENTIALS = credentials

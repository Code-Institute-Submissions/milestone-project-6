"""
Django settings for UnicornAttractor project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
import os
import accounts

# from e-commerce lesson
if os.path.exists('env.py'):
    import env

# below 4 lines from: https://stackoverflow.com/questions/37604289/tkinter-tclerror-no-display-name-and-no-display-environment-variable
# for testing matplotlib functions in Travis 
import matplotlib as mpl
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

AUTH_USER_MODEL = 'accounts.User'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["milestone-project-5-paddywc.c9users.io", "paddywc-unicornattractor.herokuapp.com"]


# Application definition
INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_forms_bootstrap',
    'django_extensions',
    'storages',
    'accounts',
    'market',
    'unicornapp',
    'usersuggestions',
    'django_countries',
    'ckeditor',
    'ckeditor_uploader',

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



ROOT_URLCONF = 'UnicornAttractor.urls'

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
                'market.contexts.cart',
                'market.contexts.usercoins',
                'market.contexts.coins_are_enabled',
            ],
        },
    },
]

WSGI_APPLICATION = 'UnicornAttractor.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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



MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Toggle to enable and disable coins
COINS_ENABLED = True

# AWS code from e-commerce lesson 
AWS_S3_OBJECT_PARAMETERS = {
    "Expires" : "Thu, 31 Dec 2099 20:00:00 GMT",
    "CacheControl": "max-age=94608000",
}

AWS_STORAGE_BUCKET_NAME = "paddywc-unicornattractor"
AWS_S3_REGION_NAME = "eu-west-1"
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    )

MEDIAFILES_LOCATION = "media"
DEFAULT_FILE_STORAGE = "custom_storages.MediaStorage"

STRIPE_PUBLISHABLE =  os.environ.get('STRIPE_PUBLISHABLE')
STRIPE_SECRET = os.environ.get('STRIPE_SECRET')

AWS_S3_CUSTOM_DOMAIN = "{}.s3.amazonaws.com".format(AWS_STORAGE_BUCKET_NAME)

STATICFILES_LOCATION = "static"
STATICFILES_STORAGE = "custom_storages.StaticStorage"

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = "https://{0}/{1}/".format(AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)

# From Django Auth Project
EMAIL_USE_TLS = True          
EMAIL_HOST = 'smtp.gmail.com'         
EMAIL_PORT = 587        
EMAIL_HOST_USER = os.environ.get('EMAIL_ADDRESS')        
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')     
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  


CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    'default': {
        
        'extraPlugins': ','.join([
        'easyimage',
              ]),
        "removePlugins": "image",
        "cloudServices_tokenUrl": os.environ.get("CLOUDSERVICES_TOKENURL"),
        "cloudServices_uploadUrl": 'https://34707.cke-cs.com/easyimage/upload/',
    
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Undo', 'Redo'],
            ['Bold', 'Italic', 'Underline'],
            ['Styles'],
            ['Format'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-'],
            ['EasyImageUpload' ,'-', 'Table'],
            ['Link', 'Unlink'],
            ['RemoveFormat'],
        ],
    }
}

CART_SESSION_ID = 'cart'

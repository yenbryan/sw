"""
Django settings for fundy project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h5e-n-7u1*90_^q=5no1m3bio$#8@&3(&ey&!e6c#v!d8k1617'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = []


# Application definition

DJANGO_CORE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'social.apps.django_app.default',
]

DEV_APPS = [
    # 'debug_toolbar',
    # 'django_extensions',
]

PROJECT_APPS = [
    'registration',
    'company',
]

INSTALLED_APPS = DJANGO_CORE_APPS + THIRD_PARTY_APPS + DEV_APPS + PROJECT_APPS

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

ROOT_URLCONF = 'fundy.urls'

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

WSGI_APPLICATION = 'fundy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "static", *MEDIA_URL.strip("/").split("/"))



# TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
# TEMPLATE_DIRS = (TEMPLATE_PATH,)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    # 'social.backends.linkedin.LinkedinOAuth2',
    # 'social.backends.linkedin.LinkedinOAuth',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_FACEBOOK_KEY = '64318926627'
SOCIAL_AUTH_FACEBOOK_SECRET = 'e72b538d8816227aa44d4f9d582a7f23'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'public_profile', 'user_photos']

# SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = '755fs9tbxtqx2n'
# SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = 'RNAJ4ecr5jsRpylj'
# # Add email to requested authorizations.
# SOCIAL_AUTH_LINKEDIN_SCOPE = ['r_basicprofile', 'r_emailaddress',]
# # Add the fields so they will be requested from linkedin.
# SOCIAL_AUTH_LINKEDIN_FIELD_SELECTORS = ['email-address', 'headline', 'industry']
# # Arrange to add the fields to UserSocialAuth.extra_data
# SOCIAL_AUTH_LINKEDIN_EXTRA_DATA = [('id', 'id'),
#                                    ('firstName', 'first_name'),
#                                    ('lastName', 'last_name'),
#                                    ('emailAddress', 'email_address'),
#                                    ('headline', 'headline'),
#                                    ('industry', 'industry')]

SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'

# Related to users
LOGIN_REDIRECT_URL = 'my_profile'
LOGIN_URL = 'splash_index'
AUTH_USER_MODEL = 'registration.Profile'
# SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/new-social-user-redirect/'
# SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/logged-in/'

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.mail.mail_validation',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'registration.pipeline.get_profile_picture',
)

# PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
# MEDIA_URL = "/media/"
# MEDIA_ROOT = os.path.join(PROJECT_ROOT, "static", *MEDIA_URL.strip("/").split("/"))
#
#
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, "static"),
# )
#
# # templates
# TEMPLATE_DIRS = (
#     os.path.join(PROJECT_ROOT, 'templates'),
# )
#
# # Related to users
# # LOGIN_REDIRECT_URL = 'account'
# # LOGIN_URL = 'login'
# AUTH_USER_MODEL = 'registration.Profile'


# # django rest framework settings
# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
#         'rest_framework.permissions.IsAuthenticated',
#     ),
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework.authentication.SessionAuthentication',
#         'rest_framework.authentication.BasicAuthentication',
#         'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
#     ),
# }
#
# # django rest jwt
# JWT_AUTH = {
#     'JWT_EXPIRATION_DELTA': datetime.timedelta(days=14)
# }
#
# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] = dj_database_url.config()



# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
# STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# try:
#     from local_settings import *
# except ImportError:
#     pass


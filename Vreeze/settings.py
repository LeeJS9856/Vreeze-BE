"""
Django settings for Vreeze project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import json
from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
secret = json.load(open(BASE_DIR/"secrets.json"))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secret["DJANGO_SECRET_KEY"]

OPENAI_API_KEY = secret["OPENAI_API_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = secret["ALLOWED_HOSTS"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    "rest_framework",
    "rest_framework_simplejwt",

    'social_django',

    'user',
    'voice',
    'present',
    'payment',
    'chat',
    'Vreeze',  # 메인 앱 이름
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

ROOT_URLCONF = 'Vreeze.urls'

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

WSGI_APPLICATION = 'Vreeze.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "user.User"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN":  True,
}

# SOCIAL_AUTH 설정
SOCIAL_AUTH_KAKAO_KEY = secret["KAKAO_KEY"]
SOCIAL_AUTH_KAKAO_SECRET = secret["KAKAO_SECRET"]
SOCIAL_AUTH_KAKAO_SCOPE = ['profile_nickname']
SOCIAL_AUTH_KAKAO_EXTRA_DATA = ['nickname']

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = secret["GOOGLE_KEY"]
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = secret["GOOGLE_SECRET"]
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ["email", "profile"]

SOCIAL_AUTH_NAVER_KEY = secret["NAVER_KEY"]
SOCIAL_AUTH_NAVER_SECRET = secret["NAVER_SECRET"]
SOCIAL_AUTH_NAVER_SCOPE = ["email", "name", "profile_image"]
SOCIAL_AUTH_NAVER_EXTRA_DATA = ["email", "name"]

LOGIN_REDIRECT_URL = "http://127.0.0.1:8000/auth/complete/"

LOGOUT_REDIRECT_URL = 'http://127.0.0.1:8000'

AUTHENTICATION_BACKENDS = (
    'social_core.backends.kakao.KakaoOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.naver.NaverOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

#s3 연결
AWS_ACCESS_KEY_ID = secret["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = secret["AWS_SECRET_ACCESS_KEY"]
AWS_STORAGE_BUCKET_NAME = secret["AWS_STORAGE_BUCKET_NAME"]
AWS_S3_REGION_NAME = secret["AWS_S3_REGION_NAME"]
AWS_S3_SIGNATURE_VERSION = secret["AWS_S3_SIGNATURE_VERSION"]
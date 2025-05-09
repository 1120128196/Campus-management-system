"""
Django settings for djangoProject1 project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7j11yc!y2f453zx5_^@r0dtyzg18v8b*)y%+kdu=_w-^=m*uve'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app01.apps.App01Config',
    'web.apps.WebConfig',
    'captcha',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'app01.middleware.auth.AuthMiddleware',
]

ROOT_URLCONF = 'djangoProject1.urls'

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

WSGI_APPLICATION = 'djangoProject1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
# 默认的是sqlite数据库 改用mysql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pythonweb',
        'USER':'root',
        'PASSWORD':'123456',
        'HOST':'127.0.0.1',
        'PORT':3306,
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# 解决警告 主键app01.Admin: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
# 	HINT: Configure the DEFAULT_AUTO_FIELD setting or the App01Config.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# 验证码
# 验证码默认样式
CAPTCHA_IMAGE_SIZE = (150, 50)  # 图片尺寸
CAPTCHA_LENGTH = 4  # 字符数
CAPTCHA_FONT_SIZE = 40  # 字体大小
CAPTCHA_BACKGROUND_COLOR = '#FFFFFF'  # 背景色
CAPTCHA_FOREGROUND_COLOR = '#000000'  # 文字颜色

# # 高级样式
# # 噪点 + 旋转字符
# CAPTCHA_NOISE_FUNCTIONS = (
#     'captcha.helpers.noise_dots',  # 添加噪点
# )
# CAPTCHA_LETTER_ROTATION = (-30, 30)  # 字符旋转角度范围

# # 数学公式挑战
# CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'  # 使用数学公式作为挑战
#
# # 字体选择
# CAPTCHA_FONT_PATH = 'path/to/custom/font.ttf'  # 自定义字体路径

# 导入media时候的配置 还包括在urls中  还需要手动在根目录创建一个media文件
# 配置完后 可以直接在浏览器中http://127.0.0.1:8000/media/p1.png 查看图片了
import os
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'

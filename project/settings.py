import os
from environs import Env


env = Env()
env.read_env() 

DATABASES = {
    'default': {
        'ENGINE': env.str('ENGINE_KEY'),
        'HOST': env.str('HOST_KEY'),
        'PORT': env.str('PORT_KEY'),
        'NAME': env.str('NAME_KEY'),
        'USER': env.str('USER_KEY'),
        'PASSWORD': env.str('PASSWORD_KEY'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = 'REPLACE_ME'

DEBUG = env.bool("DEBUG_KEY", default=False)

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

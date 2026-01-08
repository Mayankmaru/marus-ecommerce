
from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'marus-demo-key'
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = [
 'django.contrib.admin','django.contrib.auth','django.contrib.contenttypes',
 'django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles',
 'store',
]
MIDDLEWARE = [
 'django.middleware.security.SecurityMiddleware',
 'django.contrib.sessions.middleware.SessionMiddleware',
 'django.middleware.common.CommonMiddleware',
 'django.middleware.csrf.CsrfViewMiddleware',
 'django.contrib.auth.middleware.AuthenticationMiddleware',
 'django.contrib.messages.middleware.MessageMiddleware',
]
ROOT_URLCONF = 'marus_project.urls'
TEMPLATES = [{
 'BACKEND':'django.template.backends.django.DjangoTemplates',
 'DIRS':[BASE_DIR/'templates'],'APP_DIRS':True,
 'OPTIONS':{'context_processors':[
  'django.template.context_processors.debug',
  'django.template.context_processors.request',
  'django.contrib.auth.context_processors.auth',
  'django.contrib.messages.context_processors.messages',
 ]},
}]
WSGI_APPLICATION = 'marus_project.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'marus_db',
        'USER': 'root',
        'PASSWORD': 'Mayank977@',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
LANGUAGE_CODE='en-us'
TIME_ZONE='Asia/Kolkata'
STATIC_URL='/static/'
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'
STATICFILES_DIRS = [
    BASE_DIR / "static"
]
LOGIN_URL = '/login/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
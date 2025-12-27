

import os
from pathlib import Path

# ========== БАЗОВЫЕ НАСТРОЙКИ ==========
BASE_DIR = Path(__file__).resolve().parent.parent

# ========== ПЕРЕМЕННЫЕ ОКРУЖЕНИЯ ==========
# Секретный ключ - МОЖЕТ БЫТЬ В КОДЕ ТОЛЬКО ДЛЯ РАЗРАБОТКИ
# Но лучше использовать os.getenv как в примере ниже
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-разработка-ключ-для-локального-использования')

# Режим отладки - ВКЛЮЧЕН для разработки
DEBUG = True  # Или os.getenv('DEBUG', 'True') == 'True'

# Разрешенные хосты - ТОЛЬКО localhost
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

# ========== ПРИЛОЖЕНИЯ ==========
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Твое приложение
    'main',
]

# ========== MIDDLEWARE ==========
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ========== URL КОНФИГУРАЦИЯ ==========
ROOT_URLCONF = 'djangoProject.urls'

# ========== ТЕМПЛАТЫ ==========
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
            ],
        },
    },
]

# ========== БАЗА ДАННЫХ ==========
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # Путь к твоей базе данных
    }
}

# ========== СТАТИЧЕСКИЕ ФАЙЛЫ ==========
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# ========== МЕДИА ФАЙЛЫ ==========
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ========== ОСТАЛЬНЫЕ НАСТРОЙКИ ==========
WSGI_APPLICATION = 'djangoProject.wsgi.application'

# Пароли
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', 'OPTIONS': {'min_length': 8}},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Язык и время
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ========== ДЛЯ РАЗРАБОТКИ - МОЖНО ДОБАВИТЬ ПОЗЖЕ ==========
# CSRF доверенные источники (для localhost)
CSRF_TRUSTED_ORIGINS = ['http://localhost:8000', 'http://127.0.0.1:8000']

# CORS (если будешь делать API)
# CORS_ALLOWED_ORIGINS = ['http://localhost:3000']  # Для фронтенда на React

# ========== ДЛЯ УДОБСТВА РАЗРАБОТКИ ==========
# Показывать подробные ошибки
DEBUG_PROPAGATE_EXCEPTIONS = True

# Логирование в консоль
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}
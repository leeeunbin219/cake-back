import os
import environ
from pathlib import Path
import my_settings

# Build paths inside the project like this: BASE_DIR / 'subdir'.

env = environ.Env()

BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

SECRET_KEY = env("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = []


# Application definition

THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "colorfield",
]


CUSTOM_APPS = [
    "users.apps.UsersConfig",
    "cake.apps.CakeConfig",
    "visitors.apps.VisitorsConfig",
    "common.apps.CommonConfig",
]


SYSTEM_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

INSTALLED_APPS = SYSTEM_APPS + THIRD_PARTY_APPS + CUSTOM_APPS


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = False

USE_TZ = False


AUTH_USER_MODEL = "users.User"


CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_ALLOW = True

# 리액트와 연결 시 필요한 설정
CORS_ALLOWED_ORIGINS = ["http://127.0.0.1:3000"]
CSRF_TRUSTED_ORIGINS = ["http://127.0.0.1:3000"]


# 리액트와 도메인 연결 시 필요한 설정 (도메인 구매 후 이 부분 주석 해제)
# if DEBUG:
#     CORS_ALLOWED_ORIGINS = ["http://127.0.0.1:3000"]
#     CSRF_TRUSTED_ORIGINS =["http://127.0.0.1:3000"]

# else :
#     CSRF_TRUSTED_ORIGINS = ["합치는 도메인"]
#     CORS_ALLOWED_ORIGINS = ["합치는 도메인"]


STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
    ]
}

ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = True
ACCOUNT_SESSION_REMEMBER = True
SESSION_COOKIE_AGE = 3600
SESSION_EXPIRE_AT_BROWSER_CLOSE = False


## 이메일 인증 시작 ##
EMAIL_BACKEND = my_settings.EMAIL["EMAIL_BACKEND"]  # 메일을 보내는 방식
EMAIL_HOST = my_settings.EMAIL["EMAIL_HOST"]  # 메일을 호스트 하는 서버
EMAIL_PORT = my_settings.EMAIL["EMAIL_PORT"]  # 메일과 통신하는 포트
EMAIL_USE_TLS = my_settings.EMAIL["EMAIL_USE_TLS"]  # TLS 보안 사용
EMAIL_HOST_USER = my_settings.EMAIL["EMAIL_HOST_USER"]  # 발신할 네이버 이메일
EMAIL_HOST_PASSWORD = my_settings.EMAIL["EMAIL_HOST_PASSWORD"]  # 네이버 앱 비밀번호
DEFAULT_FROM_EMAIL = my_settings.EMAIL["DEFAULT_FROM_EMAIL"]  # 사이트와 관련한 자동 응답 받을 이메일 주소

ACCOUNT_AUTHENTICATION_METHOD = "email"  # 로그인시 username 이 아니라 email을 사용하게 하는 설정
ACCOUNT_EMAIL_REQUIRED = True  # 회원가입시 필수 이메일을 필수항목으로 만들기
ACCOUNT_USERNAME_REQUIRED = False  # USERNAME 을 필수항목에서 제거
ACCOUNT_USER_MODEL_USERNAME_FIELD = None

ACCOUNT_EMAIL_VERIFICATION = "mandatory"  # 이메일 인증을 필수로 설정
ACCOUNT_EMAIL_ON_GET = True  # 이메일 인증시 이메일을 보내줌
ACCOUNT_EMAIL_SUBJECT_PREFIX = "[회원가입 이메일 인증] "  # 이메일에 자동으로 표시되는 제목
ACCOUNT_CONFIRM_EMAIL_ON_GET = True  # 유저가 받은 링크를 클릭하면 회원가입 완료

# URL_FRONT = "프론트 도메인", "http://127.0.0.1:3000"  # 프론트 주소

## 이메일 인증 끝 ##

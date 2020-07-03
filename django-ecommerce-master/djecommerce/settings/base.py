import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

SECRET_KEY = '8#s^kyoz5g-@f(xd)0)1ass(9lknoi=3_l0hgv^iy^szqw3lq7'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
    'django_countries',

    'django_filters',
    'django_extensions',

    # 'webpush',

    'core',
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

ROOT_URLCONF = 'djecommerce.urls'

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

# AUTH_USER_MODEL = 'core.EcommerceUser'

GRAPH_MODELS = {
    'all_applications': True,
    'group_models': True,
}

# WEBPUSH_SETTINGS = {
#     "VAPID_PUBLIC_KEY": "BIHPaqGVkzIePYMUOCoK61unJ2Qi3VGZRQ8ObINU1HQw1tQHGEbMvtDEY-wZNzphS-JPV7QI3UibvW0Scjxlfoo",
#     "VAPID_PRIVATE_KEY": "p2Bz6G20GRqShK_36k91YNcEFF2aFSLpLhwjZmKfNk8",
#     "VAPID_ADMIN_EMAIL": "alexgathua3@gmail.com",
# }

WSGI_APPLICATION = 'djecommerce.wsgi.application'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = False

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_in_env')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')

# Auth

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
LOGOUT_URL = 'account_logout'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
ACCOUNT_SIGNUP_REDIRECT_URL = 'account_login'
LOGIN_REDIRECT_URL = 'retailer_dash'
ACCOUNT_USERNAME_BLACKLIST = ['mike', 'alex']
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_SUBJECT_PREFIX = "[Alex Ian eccomerce web]"

LOGIN_REDIRECT_URL = '/'

SITE_ID = 1
# CRISPY FORMS

CRISPY_TEMPLATE_PACK = 'bootstrap4'

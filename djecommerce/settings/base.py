import os, sentry_sdk
from decouple import config
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn=config('DSN'),
    integrations=[DjangoIntegration()],

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

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
    'django_celery_results',
    'phone_field',
    'rangefilter',
    'rest_framework',

    'widget_tweaks',

    'core',
    'mpesa',
    'utils',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 'core.middlewares.OneSessionPerUser',
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
    'allauth.account.auth_backends.AuthenticationBackend',
)

ACCOUNT_ADAPTER = 'utils.adapter.ShopAdapter'

ACCOUNT_SIGNUP_FORM_CLASS = 'utils.forms.SignupForm'

SENDGRID_API_KEY = config("SENDGRID_API_KEY")
# Toggle sandbox mode (when running in DEBUG mode)
#SENDGRID_SANDBOX_MODE_IN_DEBUG = False

#EMAIL_HOST = config('EMAIL_HOST')
#EMAIL_PORT = config('EMAIL_PORT', cast=int)
#EMAIL_HOST_USER = 'apikey'
#EMAIL_HOST_PASSWORD = SENDGRID_API_KEY

EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_PASSWORD')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)

EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'TestSite Team <djangologinsmtp@gmail.com>'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
LOGOUT_URL = 'account_logout'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
ACCOUNT_SIGNUP_REDIRECT_URL = 'account_login'

ACCOUNT_USERNAME_BLACKLIST = ['mike', 'alex']
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_SUBJECT_PREFIX = "[Alex Ian eccomerce web]"

LOGIN_REDIRECT_URL = 'where_to_go'

SITE_ID = 1
# CRISPY FORMS

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# The Mpesa environment to use
# Possible values: sandbox, production

# MPESA_ENVIRONMENT = config('MPESA_ENVIRONMENT')

# Credentials for the daraja app

# MPESA_CONSUMER_KEY = config('MPESA_CONSUMER_KEY')
# MPESA_CONSUMER_SECRET = config('MPESA_CONSUMER_SECRET')

# Shortcode to use for transactions. For sandbox  use the Shortcode 1 provided on test credentials page

# MPESA_SHORTCODE = 'Initiator Name (Shortcode 1)'
# Shortcode to use for Lipa na MPESA Online (MPESA Express) transactions
# This only has a different value on sandbox, you do not need to set it on production
# For sandbox use the Lipa na MPESA Online Shorcode provided on test credentials page

# MPESA_EXPRESS_SHORTCODE = config('MPESA_EXPRESS_SHORTCODE')

# Type of shortcode
# Possible values:
# - paybill (For Paybill)
# - till_number (For Buy Goods Till Number)

# MPESA_SHORTCODE_TYPE = config('MPESA_SHORTCODE_TYPE')

# Lipa na MPESA Online passkey
# Sandbox passkey is available on test credentials page
# Production passkey is sent via email once you go live

# MPESA_PASSKEY = config('MPESA_PASSKEY')

# this is the url where we post the B2C request to Mpesa. Replace this with the url you get from safaricom after you
# have passed the UATS
MPESA_URL = config('MPESA_URL')

# Consumer Secret
MPESA_C2B_ACCESS_KEY = config('MPESA_C2B_ACCESS_KEY')
# Consumer Key
MPESA_C2B_CONSUMER_SECRET = config('MPESA_C2B_CONSUMER_SECRET')
# Url for registering your paybill replace it the url you get from safaricom after you have passed the UATS
C2B_REGISTER_URL = config('C2B_REGISTER_URL')
# ValidationURL
# replace http://mpesa.ngrok.io/ with your url ow here this app is running
C2B_VALIDATE_URL = config('C2B_VALIDATE_URL')
# ConfirmationURL
# replace http://mpesa.ngrok.io/ with your url ow here this app is running
C2B_CONFIRMATION_URL = config('C2B_CONFIRMATION_URL')
# ShortCode (Paybill)
C2B_SHORT_CODE = config('C2B_SHORT_CODE')
# ResponseType
C2B_RESPONSE_TYPE = config('C2B_RESPONSE_TYPE')

# C2B (STK PUSH) Configs
# https://developer.safaricom.co.ke/lipa-na-m-pesa-online/apis/post/stkpush/v1/processrequest

# replace http://mpesa.ngrok.io/ with your url ow here this app is running
C2B_ONLINE_CHECKOUT_CALLBACK_URL = config('C2B_ONLINE_CHECKOUT_CALLBACK_URL')
# The Pass Key provided by Safaricom when you pass UAT's
# See https://developer.safaricom.co.ke/test_credentials
C2B_ONLINE_PASSKEY = config('C2B_ONLINE_PASSKEY')
# Your Paybill
C2B_ONLINE_SHORT_CODE = config('C2B_ONLINE_SHORT_CODE')
# number of seconds from the expiry we consider the token expired the token expires after an hour
# so if the token is 600 sec (10 minutes) to expiry we consider the token expired.
TOKEN_THRESHOLD = config('TOKEN_THRESHOLD')

CELERY_BROKER_URL = 'amqp://localhost'
CELERY_RESULT_BACKEND = 'django-db'

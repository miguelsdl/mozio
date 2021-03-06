"""
Django settings for mozio_system project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_ka&n!&9ekn6dq@kc6r@bhr*dmlqg0@fmc72&of23-2_y!8)i%'

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
    'django.contrib.gis',
    'rest_framework',
    'api'
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

ROOT_URLCONF = 'mozio_system.urls'

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

WSGI_APPLICATION = 'mozio_system.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'moziodbsys',
        'USER': 'postgres',
        'PASSWORD': 'miguel001',
        'HOST': "127.0.0.1",
        'PORT': 5432,
        'CONN_MAX_AGE': 15,
        'OPTIONS': {
            'connect_timeout': 5,
        }
    },
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
NAME_MAX_LEN = 128
PHONE_MAX_LEN = 17
LANGUAGES_MAX_LEN = 20
CURRENCY_MAX_LEN = 3
PRICE_DIGITS = 10
PRICE_DECIMAL_DIGITS = 2

CURRENCY_LIST = [
    ('usd', "DOLLAR"),
    ('eur', "EURO"),
]

LANGUAGES_LIST = [
    ("ab", "Abkhazian"),
    ("aa", "Afar"),
    ("af", "Afrikaans"),
    ("ak", "Akan"),
    ("sq", "Albanian"),
    ("am", "Amharic"),
    ("ar", "Arabic"),
    ("an", "Aragonese"),
    ("hy", "Armenian"),
    ("as", "Assamese"),
    ("av", "Avaric"),
    ("ae", "Avestan"),
    ("ay", "Aymara"),
    ("az", "Azerbaijani"),
    ("bm", "Bambara"),
    ("ba", "Bashkir"),
    ("eu", "Basque"),
    ("be", "Belarusian"),
    ("bn", "Bengali (Bangla"),
    ("bh", "Bihari"),
    ("bi", "Bislama"),
    ("bs", "Bosnian"),
    ("br", "Breton"),
    ("bg", "Bulgarian"),
    ("my", "Burmese"),
    ("ca", "Catalan"),
    ("ch", "Chamorro"),
    ("ce", "Chechen"),
    ("ny", "Chichewa, Chewa, Nyanja"),
    ("zh", "Chinese"),
    ("zh-Ha ns", "Chinese (Simplified)"),
    ("zh-Ha nt", "Chinese (Traditional)"),
    ("cv", "Chuvash"),
    ("kw", "Cornish"),
    ("co", "Corsican"),
    ("cr", "Cree"),
    ("hr", "Croatian"),
    ("cs", "Czech"),
    ("da", "Danish"),
    ("dv", "Divehi, Dhivehi, Maldivian"),
    ("nl", "Dutch"),
    ("dz", "Dzongkha"),
    ("en", "English"),
    ("eo", "Esperanto"),
    ("et", "Estonian"),
    ("ee", "Ewe"),
    ("fo", "Faroese"),
    ("fj", "Fijian"),
    ("fi", "Finnish"),
    ("fr", "French"),
    ("ff", "Fula, Fulah, Pulaar, Pular"),
    ("gl", "Galician"),
    ("gd", "Gaelic (Scottish"),
    ("gv", "Gaelic (Manx"),
    ("ka", "Georgian"),
    ("de", "German"),
    ("el", "Greek"),
    ("kl", "Greenlandic"),
    ("gn", "Guarani"),
    ("gu", "Gujarati"),
    ("ht", "Haitian Creole"),
    ("ha", "Hausa"),
    ("he", "Hebrew"),
    ("hz", "Herero"),
    ("hi", "Hindi"),
    ("ho", "Hiri Motu"),
    ("hu", "Hungarian"),
    ("is", "Icelandic"),
    ("io", "Ido"),
    ("ig", "Igbo"),
    ("id, in", "Indonesian"),
    ("ia", "Interlingua"),
    ("ie", "Interlingue"),
    ("iu", "Inuktitut"),
    ("ik", "Inupiak"),
    ("ga", "Irish"),
    ("it", "Italian"),
    ("ja", "Japanese"),
    ("jv", "Javanese"),
    ("kl", "Kalaallisut, Greenlandic"),
    ("kn", "Kannada"),
    ("kr", "Kanuri"),
    ("ks", "Kashmiri"),
    ("kk", "Kazakh"),
    ("km", "Khmer"),
    ("ki", "Kikuyu"),
    ("rw", "Kinyarwanda (Rwanda"),
    ("rn", "Kirundi"),
    ("ky", "Kyrgyz"),
    ("kv", "Komi"),
    ("kg", "Kongo"),
    ("ko", "Korean"),
    ("ku", "Kurdish"),
    ("kj", "Kwanyama"),
    ("lo", "Lao"),
    ("la", "Latin"),
    ("lv", "Latvian (Lettish"),
    ("li", "Limburgish ( Limburger"),
    ("ln", "Lingala"),
    ("lt", "Lithuanian"),
    ("lu", "Luga-Katanga"),
    ("lg", "Luganda, Ganda"),
    ("lb", "Luxembourgish"),
    ("gv", "Manx"),
    ("mk", "Macedonian"),
    ("mg", "Malagasy"),
    ("ms", "Malay"),
    ("ml", "Malayalam"),
    ("mt", "Maltese"),
    ("mi", "Maori"),
    ("mr", "Marathi"),
    ("mh", "Marshallese"),
    ("mo", "Moldavian"),
    ("mn", "Mongolian"),
    ("na", "Nauru"),
    ("nv", "Navajo"),
    ("ng", "Ndonga"),
    ("nd", "Northern Ndebele"),
    ("ne", "Nepali"),
    ("no", "Norwegian"),
    ("nb", "Norwegian bokm??l"),
    ("nn", "Norwegian nynorsk"),
    ("ii", "Nuosu"),
    ("oc", "Occitan"),
    ("oj", "Ojibwe"),
    ("cu", "Old Church Slavonic, Old Bulgarian"),
    ("or", "Oriya"),
    ("om", "Oromo (Afaan Oromo"),
    ("os", "Ossetian"),
    ("pi", "P??li"),
    ("ps", "Pashto, Pushto"),
    ("fa", "Persian (Farsi"),
    ("pl", "Polish"),
    ("pt", "Portuguese"),
    ("pa", "Punjabi (Eastern"),
    ("qu", "Quechua"),
    ("rm", "Romansh"),
    ("ro", "Romanian"),
    ("ru", "Russian"),
    ("se", "Sami"),
    ("sm", "Samoan"),
    ("sg", "Sango"),
    ("sa", "Sanskrit"),
    ("sr", "Serbian"),
    ("sh", "Serbo-Croatian"),
    ("st", "Sesotho"),
    ("tn", "Setswana"),
    ("sn", "Shona"),
    ("ii", "Sichuan Yi"),
    ("sd", "Sindhi"),
    ("si", "Sinhalese"),
    ("ss", "Siswati"),
    ("sk", "Slovak"),
    ("sl", "Slovenian"),
    ("so", "Somali"),
    ("nr", "Southern Ndebele"),
    ("es", "Spanish"),
    ("su", "Sundanese"),
    ("sw", "Swahili (Kiswahili"),
    ("ss", "Swati"),
    ("sv", "Swedish"),
    ("tl", "Tagalog"),
    ("ty", "Tahitian"),
    ("tg", "Tajik"),
    ("ta", "Tamil"),
    ("tt", "Tatar"),
    ("te", "Telugu"),
    ("th", "Thai"),
    ("bo", "Tibetan"),
    ("ti", "Tigrinya"),
    ("to", "Tonga"),
    ("ts", "Tsonga"),
    ("tr", "Turkish"),
    ("tk", "Turkmen"),
    ("tw", "Twi"),
    ("ug", "Uyghur"),
    ("uk", "Ukrainian"),
    ("ur", "Urdu"),
    ("uz", "Uzbek"),
    ("ve", "Venda"),
    ("vi", "Vietnamese"),
    ("vo", "Volap??k"),
    ("wa", "Wallon"),
    ("cy", "Welsh"),
    ("wo", "Wolof"),
    ("fy", "Western Frisian"),
    ("xh", "Xhosa"),
    ("yi, ji", "Yiddish"),
    ("yo", "Yoruba"),
    ("za", "Zhuang, Chuang"),
    ("zu", "Zulu"),
]

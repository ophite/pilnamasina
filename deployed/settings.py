# Django settings for helloworld project.
import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Kobernik Yura', 'kobernik.yura@gmail.com'),
)
 
MANAGERS = ADMINS

#debug
if DEBUG == True:
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
			'NAME': 'mysql',                      # Or path to database file if using sqlite3.
			'USER': 'root',                      # Not used with sqlite3.
			'PASSWORD': '1111',                  # Not used with sqlite3.
			'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
			'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
		}
	}
else:
#deploy
	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
	        'NAME': 'trip',                      # Or path to database file if using sqlite3.
	        'USER': 'staf',                      # Not used with sqlite3.
	        'PASSWORD': '1111',                  # Not used with sqlite3.
	        'HOST': 'localhost',                 # Set to empty string for localhost. Not used with sqlite3.
	        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
	    }
	}


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
#/home/pydev/trunk/pydev/cabinet/content/
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "C:\python\helloworld\content"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
# static - not working django admin static!!!
STATIC_URL = '/admin_static/'

# session time
SESSION_COOKIE_AGE = 60*30

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'c+)(i07&amp;a)hidify$958%p@x%^5*&amp;j^1cshda1gg=fh#-%kac8'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'helloworld.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'helloworld.wsgi.application'

TEMPLATE_DIRS = (
    'myapp/templates',

    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'myapp',
	'django.contrib.sitemaps',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


ADMIN_STATIC = os.path.join(os.path.dirname(__file__), 'admin_static')
MEDIA_CONTENT = os.path.join(os.path.dirname(__file__), 'content')
MEDIA_IMAGES = os.path.join(os.path.dirname(__file__), 'content/css/ui-darkness/images')

#RECAPTCHA_PUBLIC_KEY = '6LfoXtoSAAAAAIjWR7J8ZH2thBmhR1KDFPOEovUI'
#RECAPTCHA_PRIVATE_KEY = '6LfoXtoSAAAAAI0c0cYVdMES7hs64aMXbGpk3tq0'
RECAPTCHA_PUBLIC_KEY = '6LfpG94SAAAAAO5prtxeo544jCKOXEOEiiziXYD_'
RECAPTCHA_PRIVATE_KEY = '6LfpG94SAAAAACC_ozSz-TK8YAd_BkjfwGvOHX3E'

#RECAPTCHA_USE_SSL = True
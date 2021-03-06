import logging.config

from appoptics_apm import djangoware
from django.utils.translation import ugettext_lazy as _
from environ import Env, Path

ENV = Env()

BASE_DIR = Path(__file__) - 2

SECRET_KEY = ENV.str("SECRET_KEY")
NEVERCACHE_KEY = ENV.str("NEVERCACHE_KEY")
COMPRESS_ENABLED = ENV.str("COMPRESS_ENABLED")
COMPRESS_OFFLINE = ENV.str("COMPRESS_OFFLINE")

######################
# MEZZANINE SETTINGS #
######################

# The following settings are already defined with default values in
# the ``defaults.py`` module within each of Mezzanine's apps, but are
# common enough to be put here, commented out, for conveniently
# overriding. Please consult the settings documentation for a full list
# of settings Mezzanine implements:
# http://mezzanine.jupo.org/docs/configuration.html#default-settings

# Controls the ordering and grouping of the admin menu.
#
# ADMIN_MENU_ORDER = (
#     ("Content", ("pages.Page", "blog.BlogPost",
#        "generic.ThreadedComment", (_("Media Library"), "media-library"),)),
#     ("Site", ("sites.Site", "redirects.Redirect", "conf.Setting")),
#     ("Users", ("auth.User", "auth.Group",)),
# )

# A three item sequence, each containing a sequence of template tags
# used to render the admin dashboard.
#
# DASHBOARD_TAGS = (
#     ("blog_tags.quick_blog", "mezzanine_tags.app_list"),
#     ("comment_tags.recent_comments",),
#     ("mezzanine_tags.recent_actions",),
# )

# A sequence of templates used by the ``page_menu`` template tag. Each
# item in the sequence is a three item sequence, containing a unique ID
# for the template, a label for the template, and the template path.
# These templates are then available for selection when editing which
# menus a page should appear in. Note that if a menu template is used
# that doesn't appear in this setting, all pages will appear in it.

# PAGE_MENU_TEMPLATES = (
#     (1, _("Top navigation bar"), "pages/menus/dropdown.html"),
#     (2, _("Left-hand tree"), "pages/menus/tree.html"),
#     (3, _("Footer"), "pages/menus/footer.html"),
# )

# A sequence of fields that will be injected into Mezzanine's (or any
# library's) models. Each item in the sequence is a four item sequence.
# The first two items are the dotted path to the model and its field
# name to be added, and the dotted path to the field class to use for
# the field. The third and fourth items are a sequence of positional
# args and a dictionary of keyword args, to use when creating the
# field instance. When specifying the field class, the path
# ``django.models.db.`` can be omitted for regular Django model fields.
#
# EXTRA_MODEL_FIELDS = (
#     (
#         # Dotted path to field.
#         "mezzanine.blog.models.BlogPost.image",
#         # Dotted path to field class.
#         "somelib.fields.ImageField",
#         # Positional args for field class.
#         (_("Image"),),
#         # Keyword args for field class.
#         {"blank": True, "upload_to": "blog"},
#     ),
#     # Example of adding a field to *all* of Mezzanine's content types:
#     (
#         "mezzanine.pages.models.Page.another_field",
#         "IntegerField", # 'django.db.models.' is implied if path is omitted.
#         (_("Another name"),),
#         {"blank": True, "default": 1},
#     ),
# )

# Setting to turn on featured images for blog posts. Defaults to False.
#
# BLOG_USE_FEATURED_IMAGE = True

# If True, the django-modeltranslation will be added to the
# INSTALLED_APPS setting.
USE_MODELTRANSLATION = False

# SEARCH_MODEL_CHOICES = (
#     'coverPage.CoverPage',
# )
# Search for everything!
SEARCH_MODEL_CHOICES = None

########################
# MAIN DJANGO SETTINGS #
########################

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ENV.list(
    "ALLOWED_HOSTS", default=["localhost", "127.0.0.1", "::1"]
)


def show_toolbar(request):
    return ENV.bool("SHOW_DEBUG_TOOLBAR", default=False)


DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": show_toolbar}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "US/Eastern"

# If you set this to True, Django will use timezone-aware datetimes.
USE_TZ = True

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-us"

# Supported languages
LANGUAGES = (("en-us", _("English")),)

# A boolean that turns on/off debug mode. When set to ``True``, stack traces
# are displayed for error pages. Should always be set to ``False`` in
# production. Best set to ``True`` in local_settings.py
DEBUG = ENV.bool("DEBUG", default=False)

# Whether a user's session cookie expires when the Web browser is closed.
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False
USE_L10N = False

AUTHENTICATION_BACKENDS = ("mezzanine.core.auth_backends.MezzanineBackend",)

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# Media Files Storage
DEFAULT_FILE_STORAGE = ENV.str("MEDIA_FILE_STORAGE")
AWS_ACCESS_KEY_ID = ENV.str("AWS_ACCESS_KEY_ID", default=None)
AWS_SECRET_ACCESS_KEY = ENV.str("AWS_SECRET_ACCESS_KEY", default=None)
AWS_S3_REGION_NAME = ENV.str("AWS_S3_REGION_NAME", default=None)
AWS_STORAGE_BUCKET_NAME = ENV.str("AWS_STORAGE_BUCKET_NAME", default=None)
AWS_DEFAULT_ACL = ENV.str("AWS_DEFAULT_ACL", default=None)
AWS_S3_ENCRYPTION = ENV.bool("AWS_S3_ENCRYPTION", default=False)
AWS_S3_CUSTOM_DOMAIN = ENV.str("AWS_S3_CUSTOM_DOMAIN")

# The numeric mode to set newly-uploaded files to. The value should be
# a mode you'd pass directly to os.chmod.
FILE_UPLOAD_PERMISSIONS = 0o644

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
]

AUTH_PREFIX = "django.contrib.auth.password_validation."
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": AUTH_PREFIX + "UserAttributeSimilarityValidator"},
    {
        "NAME": AUTH_PREFIX + "MinimumLengthValidator",
        "OPTIONS": {"min_length": 12},
    },
    {"NAME": AUTH_PREFIX + "CommonPasswordValidator"},
    {"NAME": AUTH_PREFIX + "NumericPasswordValidator"},
]


#############
# DATABASES #
#############

DATABASES = {
    "default": ENV.db(
        "DATABASE_URL", default=f"sqlite:////{BASE_DIR}/db.sqlite3"
    )
}


def get_memcache_config():
    """Load config from ENV, or assume Heroku deploy

    https://devcenter.heroku.com/articles/memcachier#django
    """
    if ENV.get_value("MEMCACHE_URL", default=None):
        return ENV.cache("MEMCACHE_URL")
    location = ENV.get_value("MEMCACHIER_SERVERS", default=None)
    if location:
        return {
            "BACKEND": "django.core.cache.backends.memcached.PyLibMCCache",
            "TIMEOUT": None,  # default key expiration, NOT connection timeout
            "LOCATION": ENV.str("MEMCACHIER_SERVERS"),
            "OPTIONS": {
                "binary": True,
                "username": ENV.str("MEMCACHIER_USERNAME"),
                "password": ENV.str("MEMCACHIER_PASSWORD"),
                "behaviors": {
                    # Enable faster IO
                    "no_block": True,
                    "tcp_nodelay": True,
                    # Keep connection alive
                    "tcp_keepalive": True,
                    # Timeout settings
                    "connect_timeout": 2000,  # ms
                    "send_timeout": 750 * 1000,  # us
                    "receive_timeout": 750 * 1000,  # us
                    "_poll_timeout": 2000,  # ms
                    # Better failover
                    "ketama": True,
                    "remove_failed": 1,
                    "retry_timeout": 2,
                    "dead_timeout": 30,
                },
            },
        }
    return {"BACKEND": "django.core.cache.backends.dummy.DummyCache"}


CACHE_MIDDLEWARE_SECONDS = 60

CACHES = {"default": get_memcache_config()}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"

#########
# PATHS #
#########

# Every cache key will get prefixed with this value - here we set it to
# the name of the directory the project is in to try and use something
# project specific.
CACHE_MIDDLEWARE_KEY_PREFIX = "deploymezzaninetoheroku"

# URI prefix that Django uses to serve media
STATIC_URL = "/static/"  # end-slash required

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
STATIC_ROOT = BASE_DIR("runtime", "static")
STATICFILES_DIRS = [BASE_DIR("staticfiles")]
WHITENOISE_ROOT = BASE_DIR("root_static")

# URI prefix that Django uses to serve media
MEDIA_URL = "/media/"  # end-slash required

# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = ""

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR("templates")],
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.static",
                "django.template.context_processors.media",
                "django.template.context_processors.request",
                "django.template.context_processors.tz",
                "mezzanine.conf.context_processors.settings",
                "mezzanine.pages.context_processors.page",
            ],
            "builtins": [
                "mezzanine.template.loader_tags",
                "django.templatetags.static",
                "django.contrib.staticfiles.templatetags.staticfiles",
            ],
            "loaders": [
                "mezzanine.template.loaders.host_themes.Loader",
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
        },
    }
]

TEMPLATE_ACCESSIBLE_SETTINGS = (
    "ACCOUNTS_APPROVAL_REQUIRED",
    "ACCOUNTS_VERIFICATION_REQUIRED",
    "ACCOUNTS_VERIFICATION_REQUIRED",
    "ADMIN_MEDIA_PREFIX",
    "ADMIN_MENU_COLLAPSED",
    "BITLY_ACCESS_TOKEN",
    "BLOG_BITLY_KEY",
    "BLOG_BITLY_USER",
    "BLOG_USE_FEATURED_IMAGE",
    "COMMENTS_DISQUS_API_PUBLIC_KEY",
    "COMMENTS_DISQUS_API_PUBLIC_KEY",
    "COMMENTS_DISQUS_API_SECRET_KEY",
    "COMMENTS_DISQUS_API_SECRET_KEY",
    "COMMENTS_DISQUS_SHORTNAME",
    "COMMENTS_DISQUS_SHORTNAME",
    "COMMENTS_NUM_LATEST",
    "COMMENTS_NUM_LATEST",
    "COMMENTS_USE_RATINGS",
    "DEV_SERVER",
    "DEV_SERVER",
    "FORMS_USE_HTML5",
    "FORMS_USE_HTML5",
    "GOOGLE_ANALYTICS_ID",
    "GOOGLE_ANALYTICS_ID",
    "GRAPPELLI_INSTALLED",
    "GRAPPELLI_INSTALLED",
    "JQUERY_FILENAME",
    "JQUERY_FILENAME",
    "JQUERY_UI_FILENAME",
    "LOGIN_URL",
    "LOGIN_URL",
    "LOGOUT_URL",
    "LOGOUT_URL",
    "PAGES_MENU_SHOW_ALL",
    "RATINGS_MAX",
    "SITE_TAGLINE",
    "SITE_TAGLINE",
    "SITE_TITLE",
    "SITE_TITLE",
    "USE_L10N",
    "USE_MODELTRANSLATION",
    "intro",
    "disclaimer",
)

WSGI_APPLICATION = "config.wsgi.application"

################
# APPLICATIONS #
################

INSTALLED_APPS = (
    "whitenoise.runserver_nostatic",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.redirects",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.staticfiles",
    "mezzanine.boot",
    "mezzanine.conf",
    "mezzanine.core",
    "mezzanine.generic",
    "mezzanine.pages",
    "mezzanine.blog",
    "mezzanine.forms",
    "mezzanine.galleries",
    "mezzanine.twitter",
    # "mezzanine.accounts",
    "coverPage.apps.CoverpageConfig",
)

# List of middleware classes to use. Order is important; in the request phase,
# these middleware classes will be applied in the order given, and in the
# response phase the middleware will be applied in reverse order.
MIDDLEWARE = (
    "mezzanine.core.middleware.UpdateCacheMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # Uncomment if using internationalisation or localisation
    # 'django.middleware.locale.LocaleMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "mezzanine.core.request.CurrentRequestMiddleware",
    "mezzanine.core.middleware.RedirectFallbackMiddleware",
    "mezzanine.core.middleware.AdminLoginInterfaceSelectorMiddleware",
    "mezzanine.core.middleware.SitePermissionMiddleware",
    "mezzanine.pages.middleware.PageMiddleware",
    "mezzanine.core.middleware.FetchFromCacheMiddleware",
)

# Store these package names here as they may change in the future since
# at the moment we are using custom forks of them.
PACKAGE_NAME_FILEBROWSER = "filebrowser_safe"
PACKAGE_NAME_GRAPPELLI = "grappelli_safe"

#########################
# OPTIONAL APPLICATIONS #
#########################

# These will be added to ``INSTALLED_APPS``, only if available.
OPTIONAL_APPS = (
    "debug_toolbar",
    "django_extensions",
    "compressor",
    PACKAGE_NAME_FILEBROWSER,
    PACKAGE_NAME_GRAPPELLI,
)

#####################
# SECURITY SETTINGS #
#####################

CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = True

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")

SESSION_COOKIE_DOMAIN = None  # not set on subdomains
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_NAME = "mezzanine_sessionid"
SESSION_COOKIE_SECURE = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

X_FRAME_OPTIONS = "DENY"

##################
# EMAIL SETTINGS #
##################

EMAIL_BACKEND = ENV.str(
    "EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)

DEFAULT_FROM_EMAIL = ENV.str("DEFAULT_FROM_EMAIL", default="")
SERVER_EMAIL = ENV.str("SERVER_EMAIL", default="")

EMAIL_HOST = ENV.str("EMAIL_HOST", default="")
EMAIL_PORT = ENV.int("EMAIL_PORT", default=587)
EMAIL_USE_TLS = True

EMAIL_HOST_USER = ENV.str("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = ENV.str("EMAIL_HOST_PASSWORD", default="")

####################
# DYNAMIC SETTINGS #
####################

# set_dynamic_settings() will rewrite globals based on what has been
# defined so far, in order to provide some better defaults where
# applicable. We also allow this settings module to be imported
# without Mezzanine installed, as the case may be when using the
# fabfile, where setting the dynamic settings below isn't strictly
# required.
try:
    from mezzanine.utils.conf import set_dynamic_settings
except ImportError:
    pass
else:
    set_dynamic_settings(globals())


def get_mezzanine_settings():
    """
    Returns the value of the mezzanine.conf.context_processors.settings context
    processor. Context processors usually can only be run during a request, but
    luckily, mezzanine ignores the request parameter, so we don't have to worry
    about it.
    https://www.fusionbox.com/blog/detail/how-to-use-django-compressor-offline-compression-with-widgy/570/
    """
    from mezzanine.conf.context_processors import settings

    return settings()["settings"]


COMPRESS_OFFLINE_CONTEXT = {"settings": get_mezzanine_settings}

LOGGING_CONFIG = None
logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "console": {
                "format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "console",
            }
        },
        "loggers": {"": {"level": "WARNING", "handlers": ["console"]}},
    }
)

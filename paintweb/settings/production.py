from paintweb.settings.common import *

DEBUG = False

ALLOWED_HOSTS = [os.environ.get('PRODUCTION_HOST')]
CSRF_TRUSTED_ORIGINS = ["https://"+str(os.environ.get("PRODUCTION_HOST"))]

INSTALLED_APPS.extend(["whitenoise.runserver_nostatic"])

# Must insert after SecurityMiddleware, which is first in settings/common.py
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

STATICFILES_DIRS = ['paintapp/static', 'paintsite/static']
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATIC_URL = "/static/"
# WHITENOISE_ROOT?

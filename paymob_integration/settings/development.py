from .base import *

# Development-specific settings
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'dev_db.sqlite3'),
    }
}

# Additional development configurations (e.g., Django Debug Toolbar, etc.)
INSTALLED_APPS += [
    'django_extensions',  # Add any dev-only apps here
]

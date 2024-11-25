import os

# Get the DJANGO_ENV environment variable (default to 'development')
env = os.getenv("DJANGO_ENV", "development")

if env == "production":
    from .production import *
else:
    from .development import *

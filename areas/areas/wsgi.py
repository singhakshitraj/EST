"""
WSGI config for areas project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys
print("Current Working Directory:", os.getcwd())
print("Python Path:", sys.path)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'areas.areas.settings')

application = get_wsgi_application()

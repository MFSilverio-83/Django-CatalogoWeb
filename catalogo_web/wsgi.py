"""
WSGI config for catalogo_web project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'catalogo_web.settings')

application = get_wsgi_application()

try:
    import post_deploy
except Exception as e:
    print(f"⚠️ Erro ao rodar post_deploy: {e}")

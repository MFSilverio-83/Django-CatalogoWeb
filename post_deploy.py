import os
import django
from django.core.management import call_command

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "catalogo_web.settings")
django.setup()

call_command("migrate")
call_command("collectstatic", interactive=False, verbosity=0)
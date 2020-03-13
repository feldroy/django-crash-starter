"""
ASGI config for {{ cookiecutter.project_name }} project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/asgi/
"""

import os
import sys

from django.core.asgi import get_asgi_application


# This allows easy placement of apps within the interior
# {{ cookiecutter.project_slug }} directory.
app_path = os.path.abspath(
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)), os.pardir
    )
)
sys.path.append(os.path.join(app_path, "{{ cookiecutter.project_slug }}"))
# We defer to a DJANGO_SETTINGS_MODULE already in the environment. This breaks
# if running multiple sites in the same mod_wsgi process. To fix this, use
# mod_wsgi daemon mode with each site in its own daemon process, or use
# os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings.production"
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "config.settings.production"
)

# This application object is used by any ASGI server configured to use this
# file.
application = get_asgi_application()
# Apply ASGI middleware here.
# from helloworld.asgi import HelloWorldApplication
# application = HelloWorldApplication(application)

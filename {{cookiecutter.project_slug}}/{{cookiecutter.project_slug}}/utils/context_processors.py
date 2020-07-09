from django.conf import settings


def settings_context(_request):
    # Put global template variables here.
    return {"DEBUG": settings.DEBUG}  # explicit

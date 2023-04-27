#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import sys


def main():
    """Run administrative tasks."""
    from django.conf import settings
    from system import PublishingSystem
    from django_framework.django_http_client import UrlConf

    secret_key = 'django-insecure-^3#otl^ose7xu_t8wyt5*vxlcdp%cse6oobxz94&j19p0&tc!h'
    settings.configure(ROOT_URLCONF=UrlConf(PublishingSystem()), DEBUG=True, SECRET_KEY=secret_key)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import sys



def main():
    """Run administrative tasks."""
    from system import PublishingSystem
    from django_framework.django_settings import MyDjango

    MyDjango().configure_settings_with(system=PublishingSystem(), debug=True)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environme|nt variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

class DjangoSettings:
    def configure_settings_with(self, system, debug):
        from django_framework.django_http_client import UrlConf

        import django

        from django.conf import settings
        if not settings.configured:
            from pathlib import Path

            BASE_DIR = Path(__file__).resolve().parent.parent
            secret_key = 'django-insecure-^3#otl^ose7xu_t8wyt5*vxlcdp%cse6oobxz94&j19p0&tc!h'

            settings.configure(ROOT_URLCONF=UrlConf(system),
                               INSTALLED_APPS=['publishing_system'],
                               DEBUG=debug,
                               SECRET_KEY=secret_key,
                               DATABASES={
                                   'default': {
                                       'ENGINE': 'django.db.backends.sqlite3',
                                       'NAME': BASE_DIR / 'db.sqlite3',
                                   }
                               }
                               )
            django.setup()

        from django.test.utils import override_settings

        settings_manager = override_settings(ROOT_URLCONF=UrlConf(system))
        settings_manager.enable()

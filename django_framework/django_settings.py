class MyDjango:
    def configure_settings_with(self, system, debug):
        from django_framework.django_http_client import UrlConf

        import django

        from django.conf import settings

        url_configuration = UrlConf(system)
        if not settings.configured:
            self._initial_settings(settings, debug, url_configuration)
            django.setup()

        from django.test.utils import override_settings

        settings_manager = override_settings(ROOT_URLCONF=url_configuration)
        settings_manager.enable()

    def _initial_settings(self, settings, debug, url_configuration):
        from pathlib import Path

        BASE_DIR = Path(__file__).resolve().parent.parent
        secret_key = 'django-insecure-^3#otl^ose7xu_t8wyt5*vxlcdp%cse6oobxz94&j19p0&tc!h'
        settings.configure(ROOT_URLCONF=url_configuration,
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

    def initialize_django_db(self):
        from django.test.runner import DiscoverRunner
        discovery = DiscoverRunner()
        old_config = discovery.setup_databases()
        from publishing_system.publishing_system.models import PersistentArticle
        PersistentArticle.objects.all().delete()
        return old_config

    def destroy_django_db(self, old_config):
        from django.test.runner import DiscoverRunner
        discovery = DiscoverRunner()
        discovery.teardown_databases(old_config)

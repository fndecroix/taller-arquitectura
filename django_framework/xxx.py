class Xxx:

    def __init__(self):
        self._db_config = None

    def initialize_django_from_managepy(self, assistant):
        from django.conf import settings
        settings.configure(
            DEBUG=True,
            SECRET_KEY="django-insecure-!l2bq7t!&iyafejbpwfefwdao$j#us@ygq&m27uct3=b#@k6f8",
            INSTALLED_APPS=["publishing_system"],
            DATABASES={
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': 'db.sqlite3',
                }
            }
        )

        import django
        django.setup()

        from django.test.utils import override_settings
        from django_framework.url_conf import UrlConf
        settings_manager = override_settings(
            ROOT_URLCONF=UrlConf(assistant),
        )
        settings_manager.enable()

    def initialize_django_from_http_client(self, assistant):
        from django.conf import settings
        if not settings.configured:
            settings.configure(
                DEBUG=True,
                SECRET_KEY="django-insecure-!l2bq7t!&iyafejbpwfefwdao$j#us@ygq&m27uct3=b#@k6f8",
                INSTALLED_APPS=["publishing_system"],
                DATABASES={
                    'default': {
                        'ENGINE': 'django.db.backends.sqlite3',
                        'NAME': 'db.sqlite3',
                    }
                }
            )
        from django.test.utils import override_settings
        from django_framework.url_conf import UrlConf
        settings_manager = override_settings(ROOT_URLCONF=UrlConf(assistant))
        settings_manager.enable()
        # Seems we don't need this because we don't use DB, nor DjangoAdmin
        # import django
        # django.setup()

    def initialize_django_from_test(self):
        from django.conf import settings
        if not settings.configured:
            settings.configure(
                DEBUG=True,
                SECRET_KEY="django-insecure-!l2bq7t!&iyafejbpwfefwdao$j#us@ygq&m27uct3=b#@k6f8",
                INSTALLED_APPS=["publishing_system"],
                DATABASES={
                    'default': {
                        'ENGINE': 'django.db.backends.sqlite3',
                        'NAME': 'db.sqlite3',
                    }
                }
            )

        import django
        django.setup()

    def initialize_django_db(self):
        from django.test.runner import DiscoverRunner
        discovery = DiscoverRunner()
        self._db_config = discovery.setup_databases()
        discovery.teardown_databases(self._db_config)
        self._db_config = discovery.setup_databases()
        # from code_repo.django.reader.models import MagazineArticle
        # MagazineArticle.objects.all().delete()

    def destroy_django_db(self):
        from django.test.runner import DiscoverRunner
        discovery = DiscoverRunner()
        discovery.teardown_databases(self._db_config)
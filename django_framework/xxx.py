class Xxx:

    def __init__(self):
        self._db_config = None

    def initialize_django_from_managepy(self, assistant):

        self._load_initial_settings_configuration()

        import django
        django.setup()

        from django.test.utils import override_settings
        from django_framework.django_http_client import UrlConf
        settings_manager = override_settings(
            ROOT_URLCONF=UrlConf(assistant),
        )
        settings_manager.enable()

    def initialize_django_from_http_client(self, assistant):
        from django.conf import settings
        if not settings.configured:
            self._load_initial_settings_configuration()
        from django.test.utils import override_settings
        from django_framework.django_http_client import UrlConf
        settings_manager = override_settings(
            ROOT_URLCONF=UrlConf(assistant),
        )
        settings_manager.enable()
        # Seems we don't need this because we don't use DB, nor DjangoAdmin
        # import django
        # django.setup()

    def _load_initial_settings_configuration(self):
        from django.conf import settings
        settings.configure(
            DEBUG=True,
            SECRET_KEY=self._secret_key(),
            INSTALLED_APPS=self._installed_apps(),
            DATABASES=self._database_configuration()
        )

    def initialize_django_from_test(self):
        from django.conf import settings
        if not settings.configured:
            self._load_initial_settings_configuration()

        import django
        django.setup()

    def _installed_apps(self):
        return ["publishing_system"]

    def initialize_django_db(self):
        from django.test.runner import DiscoverRunner
        discovery = DiscoverRunner()
        self._db_config = discovery.setup_databases()
        discovery.teardown_databases(self._db_config)
        self._db_config = discovery.setup_databases()
        # from publishing_system.publishing_system.models import PersistentArticle
        # PersistentArticle.objects.all().delete()

    def destroy_django_db(self):
        pass

    def _database_configuration(self):
        db_configuration = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'db.sqlite3',
            }
        }
        return db_configuration

    def _secret_key(self):
        return "django-insecure-!l2bq7t!&iyafejbpwfefwdao$j#us@ygq&m27uct3=b#@k6f8"

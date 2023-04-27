import json


class DjangoHttpClient:
    def __init__(self, system=None):
        from django.conf import settings

        if not settings.configured:
            settings.configure(ROOT_URLCONF=UrlConf(system))

    def set_system(self, new_system):
        from django.test.utils import override_settings
        settings_manager = override_settings(ROOT_URLCONF=UrlConf(new_system))
        settings_manager.enable()

    def get_articles(self):
        from django.urls import reverse

        django_response = self.django_client().get(reverse('list-articles'))
        # TODO: este metodo deberia responder nuestra Response
        return json.loads(django_response.content)

    def django_client(self):
        from django.test.client import Client

        return Client()


class UrlConf:
    def __init__(self, system) -> None:
        self.system = system

    @property
    def urlpatterns(self):
        from django.urls import path

        from publishing_system.publishing_system.views.publishing_system_views import PublishingSystemViews

        urlpatterns = [
            path('articles/', PublishingSystemViews(self.system).get_articles, name='list-articles'),
        ]

        return urlpatterns

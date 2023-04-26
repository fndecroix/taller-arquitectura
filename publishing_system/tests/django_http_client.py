import json

from django.conf import settings
from django.test.client import Client

from publishing_system.publishing_system.global_publishing_system import GlobalPublishingSystem
from django.urls import reverse


class DjangoHttpClient:
    def __init__(self):
        if not settings.configured:
            settings.configure(ROOT_URLCONF=UrlConf())

    def set_system(self, new_system):
        GlobalPublishingSystem.set_system(new_system)

    def get_articles(self):
        django_response = self.django_client().get(reverse('list-articles'))
        # TODO: este metodo deberia responder nuestra Response
        return json.loads(django_response.content)

    def django_client(self):
        return Client()


class UrlConf:
    @property
    def urlpatterns(self):
        from django.urls import path

        from publishing_system.publishing_system.views.publishing_system_views import PublishingSystemViews

        urlpatterns = [
            path('articles/', PublishingSystemViews().get_articles, name='list-articles'),
        ]

        return urlpatterns

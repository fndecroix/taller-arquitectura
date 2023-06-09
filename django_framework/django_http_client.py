import json

from django_framework.django_settings import MyDjango
from interfaces.http_interface import HttpResponse


class DjangoHttpClient:
    def set_system(self, new_system):
        self._inject_system_in_django_views(new_system)

    def get_articles(self):
        from django.urls import reverse

        django_response = self._django_client().get(reverse('list-articles'))
        return self._from_django_http_response(django_response)

    def _from_django_http_response(self, django_response):
        response_content = json.loads(django_response.content)
        return HttpResponse(response_content)

    def _django_client(self):
        from django.test.client import Client

        return Client()

    def _inject_system_in_django_views(self, new_system):
        MyDjango().configure_settings_with(system=new_system, debug=True)


class UrlConf:
    def __init__(self, system) -> None:
        self.system = system

    @property
    def urlpatterns(self):
        from django.urls import path

        from django_framework.publishing_system_views import PublishingSystemViews

        urlpatterns = [
            path('articles/', PublishingSystemViews(self.system).get_articles, name='list-articles'),
        ]

        return urlpatterns

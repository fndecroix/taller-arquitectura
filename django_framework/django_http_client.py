import json

from django_framework.url_conf import UrlConf
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
        from django.test.utils import override_settings
        settings_manager = override_settings(ROOT_URLCONF=UrlConf(new_system))
        settings_manager.enable()

from interfaces.http_interface import HttpInterface, HttpRequest
from django_framework.django_http_response import DjangoHttpResponse


class PublishingSystemViews:
    def __init__(self, system) -> None:
        self.system = system

    def get_articles(self, request):
        http_request = self._build_request(request)
        http_response = self.interface().get_articles(http_request)

        return DjangoHttpResponse.response_for(http_response)

    def _build_request(self, request):
        return HttpRequest(parameters={})

    def interface(self):
        return HttpInterface(publishing_system=self.system)

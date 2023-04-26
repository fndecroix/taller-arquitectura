from interfaces.http_interface import HttpInterface, HttpRequest
from publishing_system.publishing_system.django_http_response import DjangoHttpResponse
from publishing_system.publishing_system.global_publishing_system import GlobalPublishingSystem


class PublishingSystemViews:
    def get_articles(self, request):
        http_request = self._build_request(request)
        http_response = self.interface().get_articles(http_request)

        return DjangoHttpResponse.response_for(http_response)

    def _build_request(self, request):
        return HttpRequest(parameters={})

    def interface(self):
        return HttpInterface(publishing_system=self.system())

    def system(self):
        return GlobalPublishingSystem.get_system()

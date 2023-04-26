from interfaces.http_interface import HttpInterface, HttpRequest
from publishing_system.publishing_system.django_http_response import DjangoHttpResponse
from publishing_system.publishing_system.global_publishing_system import GlobalPublishingSystem


class PublishingSystemViews:
    def get_articles(self, request):
        response = self.interface().get_articles(self._build_request(request))
        return DjangoHttpResponse.response_for(response)

    def _build_request(self, request):
        return HttpRequest(parameters={})

    def interface(self):
        return HttpInterface(publishing_system=self.system())

    def system(self):
        return GlobalPublishingSystem.get_system()

from interfaces.http_interface import HttpInterface
from publishing_system.publishing_system.django_http_response import DjangoHttpResponse
from publishing_system.publishing_system.global_publishing_system import GlobalPublishingSystem


class PublishingSystemViews:
    def get_articles(self, request):
        # TODO: el request es el de django y deberia ser el nuestro
        response = self.interface().get_articles(request)
        return DjangoHttpResponse.response_for(response)

    def interface(self):
        return HttpInterface(publishing_system=self.system())

    def system(self):
        return GlobalPublishingSystem.get_system()

from interfaces.http_interface import HttpResponse, HttpInterface
from publishing_system.publishing_system.django_http_response import DjangoHttpResponse
from system import PublishingSystem
from tests.article_texts import ArticleTexts


class PublishingSystemViews:
    def __init__(self) -> None:
        system = PublishingSystem()
        self._publish_sample_article_in(system)
        self.http_interface = HttpInterface(publishing_system=system)

    def get_articles(self, request):
        # TODO: el request es el de django y deberia ser el nuestro
        response = self.http_interface.get_articles(request)
        return DjangoHttpResponse.response_for(response)

    def _publish_sample_article_in(self, system):
        system.publish_article(ArticleTexts().valid_title(), ArticleTexts().valid_text())

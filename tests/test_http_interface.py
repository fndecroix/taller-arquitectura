from unittest import TestCase

from interfaces.http_interface import HttpInterface, HttpRequest
from system import PublishingSystem
from tests.article_texts import ArticleTexts


class HttpInterfaceTest(TestCase):
    def setUp(self) -> None:
        self.publishing_system = PublishingSystem()
        self.interface = HttpInterface(publishing_system=self.publishing_system)

    def test_article_list_when_there_are_no_articles_is_empty(self):
        self.assertEquals(len(self.interface.get_articles(self._http_request_with(parameters={})).content()), 0)

    def test_can_get_article_list_with_a_single_article(self):
        a_title = 'A title'
        a_text = ArticleTexts().valid_text()
        article_number = self.add_an_article_with(a_title, a_text)

        article_list = self.interface.get_articles(self._http_request_with(parameters={})).content()

        self.assertEquals(len(article_list), 1)
        self.assertEquals(article_list[0]['number'], article_number)

    def test_can_get_details_from_a_single_article(self):
        a_title = 'A title'
        a_text = ArticleTexts().valid_text()
        article_number = self.add_an_article_with(a_title, a_text)

        parameters = {'article_number': article_number}
        article_details = self.interface.get_article(self._http_request_with(parameters=parameters)).content()

        self.assertEquals(article_details['text'], a_text)
        self.assertEquals(article_details['title'], a_title)

    def _http_request_with(self, parameters):
        return HttpRequest(parameters=parameters)

    def add_an_article_with(self, a_title, a_text):
        return self.publishing_system.publish_article(a_title, a_text)

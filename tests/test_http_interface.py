from unittest import TestCase

from interfaces.http_interface import HttpInterface
from system import PublishingSystem
from tests.article_texts import ArticleTexts


class HttpInterfaceTest(TestCase):
    def setUp(self) -> None:
        self.publishing_system = PublishingSystem()
        self.interface = HttpInterface(publishing_system=self.publishing_system)

    def test_article_list_when_there_are_no_articles_is_empty(self):
        self.assertEquals(len(self.interface.get('/articles').content()), 0)

    def test_can_get_article_list_with_a_single_article(self):
        a_title = 'A title'
        self.add_an_article_with_title(a_title)

        self.assertEquals(len(self.interface.get('/articles').content()), 1)
        self.assertEquals(self.interface.get('/articles').content()[0]['title'], a_title)

    def add_an_article_with_title(self, a_title):
        self.publishing_system.publish_article(a_title, ArticleTexts().valid_text())

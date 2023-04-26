from django.test import TestCase

from domain.magazine import Magazine
from interfaces.http_interface import HttpInterface
from publishing_system.publishing_system.global_publishing_system import GlobalPublishingSystem
from publishing_system.tests.django_http_client import DjangoHttpClient
from system import PublishingSystem
from tests.article_texts import ArticleTexts


class DjangoHttpInterfaceTest(TestCase):
    def setUp(self) -> None:
        self.http_client = DjangoHttpClient()
        self.http_client.set_system(PublishingSystem())

    def test_article_list_when_there_are_no_articles_is_empty(self):
        self.assertEquals(len(self.http_client.get_articles()), 0)

    def test_can_get_article_list_with_a_single_article(self):
        system = self.system_with_one_article()
        self.http_client.set_system(system)

        article_list = self.http_client.get_articles()

        self.assertEquals(len(article_list), 1)
        # article_number_list = [article['article_number'] for article in system.published_articles()]
        # self.assertIn(article_list[0]['number'], article_number_list)

    def add_an_article_with(self, a_title, a_text):
        return self.publishing_system().publish_article(a_title, a_text)

    def system_with_one_article(self):
        a_title = 'A title'
        a_text = ArticleTexts().valid_text()
        magazine = Magazine()
        magazine.publish_article(a_title=a_title, a_text=a_text)
        system = PublishingSystem()
        system.set_magazine(magazine)
        return system

    def publishing_system(self):
        return GlobalPublishingSystem.get_system()

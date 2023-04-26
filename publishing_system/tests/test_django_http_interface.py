from unittest import TestCase

from publishing_system.tests.django_http_client import DjangoHttpClient
from system import PublishingSystem
from tests.publishing_system_props import PublishingSystemProps


class DjangoHttpInterfaceTest(TestCase):
    def setUp(self) -> None:
        self.http_client = DjangoHttpClient()
        self.http_client.set_system(PublishingSystem())

    def test_article_list_when_there_are_no_articles_is_empty(self):
        self.assertEquals(len(self.http_client.get_articles()), 0)

    def test_can_get_article_list_with_a_single_article(self):
        system = PublishingSystemProps().system_with_one_article()
        self.http_client.set_system(system)

        article_list = self.http_client.get_articles()

        self.assertEquals(len(article_list), 1)
        # article_number_list = [article['article_number'] for article in system.published_articles()]
        # self.assertIn(article_list[0]['number'], article_number_list)

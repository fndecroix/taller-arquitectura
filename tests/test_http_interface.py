import os
from unittest import TestCase

from django_framework.django_http_client import DjangoHttpClient
from django_test_case import DjangoTestCase
from system import PublishingSystem
from tests.http_client import HttpClient
from tests.publishing_system_props import PublishingSystemProps


class HttpInterfaceTest(DjangoTestCase):
    def setUp(self) -> None:
        super().setUp()
        test_technology = os.environ['TESTING_TECHNOLOGY']
        if test_technology == 'PERFECT':
            self.http_client = HttpClient()
        elif test_technology == 'DJANGO':
            self.http_client = DjangoHttpClient()
        else:
            raise Exception(f'Invalid test technology: {test_technology}')

    def test_article_list_when_there_are_no_articles_is_empty(self):
        self.http_client.set_system(PublishingSystem())
        self.assertEquals(len(self.http_client.get_articles().content()), 0)

    def test_can_get_article_list_with_a_single_article(self):
        system = PublishingSystemProps().system_with_one_article()
        self.http_client.set_system(system)

        article_list = self.http_client.get_articles().content()

        self.assertEquals(len(article_list), 1)
        # article_number_list = [article['article_number'] for article in system.published_articles()]
        # self.assertIn(article_list[0]['number'], article_number_list)

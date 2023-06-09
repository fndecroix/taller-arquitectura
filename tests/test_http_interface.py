import os
from unittest import TestCase

from django_framework.django_http_client import DjangoHttpClient
from system import PublishingSystem
from tests.http_client import HttpClient
from tests.publishing_system_props import PublishingSystemProps


class HttpInterfaceTest(TestCase):
    def setUp(self) -> None:
        test_technology = os.environ['TEST_TECHNOLOGY']
        if test_technology == 'PERFECT':
            self.http_client = HttpClient()
        elif test_technology == 'DJANGO':
            from django_framework.django_settings import MyDjango
            self.http_client = DjangoHttpClient()
            MyDjango().configure_settings_with(system=None, debug=True)
            self.old_database_config = MyDjango().initialize_django_db()
        else:
            raise Exception(f'Invalid test technology: {test_technology}')

    def tearDown(self) -> None:
        test_technology = os.environ['TEST_TECHNOLOGY']
        if test_technology == 'PERFECT':
            pass
        elif test_technology == 'DJANGO':
            from django_framework.django_settings import MyDjango
            MyDjango().destroy_django_db(old_config=self.old_database_config)
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

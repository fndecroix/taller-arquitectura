import json

from django.test import TestCase
from django.urls import reverse

from system import PublishingSystem
from tests.article_texts import ArticleTexts


class DjangoHttpInterfaceTest(TestCase):
    def setUp(self) -> None:
        self.publishing_system = PublishingSystem()

    def test_can_get_article_list_with_a_single_article(self):
        a_title = 'A title'
        a_text = ArticleTexts().valid_text()
        article_number = self.add_an_article_with(a_title, a_text)

        content = self.get_articles().content
        article_list = json.loads(content)

        self.assertEquals(len(article_list), 1)
        self.assertEquals(article_list[0]['number'], article_number)

    def add_an_article_with(self, a_title, a_text):
        return self.publishing_system.publish_article(a_title, a_text)

    def get_articles(self):
        return self.client.get(reverse('list-articles'))

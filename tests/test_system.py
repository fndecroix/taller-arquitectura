from django_test_case import DjangoTestCase
from system import PublishingSystem
from tests.article_texts import ArticleTexts


class SystemTests(DjangoTestCase):
    def test_can_ask_system_for_list_of_articles(self):
        system = PublishingSystem()

        self.assertEquals(0, len(system.published_articles()))

    def test_can_publish_an_article(self):
        system = PublishingSystem()

        system.publish_article(a_title=ArticleTexts().valid_title(), a_text=ArticleTexts().valid_text())

        self.assertEquals(1, len(system.published_articles()))

    def test_can_view_the_summarized_version_of_article(self):
        system = PublishingSystem()
        article_text = ArticleTexts().valid_text()
        article_summarized_text = ArticleTexts().summarized_text_for(article_text)
        article_title = ArticleTexts().valid_title()

        article_number = system.publish_article(a_title=article_title, a_text=article_text)

        self.assertEquals(article_summarized_text, system.published_articles()[0]["text"])
        self.assertEquals(article_title, system.published_articles()[0]["title"])
        self.assertEquals(article_number, system.published_articles()[0]["number"])

    def test_can_view_title_of_article(self):
        system = PublishingSystem()
        article_text = ArticleTexts().valid_text()
        article_title = ArticleTexts().valid_title()

        system.publish_article(a_title=article_title, a_text=article_text)

    def test_can_access_an_article_by_id(self):
        system = PublishingSystem()
        article_text = ArticleTexts().valid_text()
        article_title = ArticleTexts().valid_title()

        article_id = system.publish_article(a_title=article_title, a_text=article_text)
        article_data = system.full_article(article_id=article_id)

        self.assertEquals(article_title, article_data['title'])

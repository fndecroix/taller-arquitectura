from domain.magazine import Magazine
from system import PublishingSystem
from tests.article_texts import ArticleTexts


class PublishingSystemProps:
    def system_with_one_article(self):
        magazine = self.magazine_with_one_article()
        system = PublishingSystem()
        system.set_magazine(magazine)
        return system

    def magazine_with_one_article(self):
        magazine = Magazine()
        a_title = 'A title'
        a_text = ArticleTexts().valid_text()
        magazine.publish_article(a_title=a_title, a_text=a_text)
        return magazine

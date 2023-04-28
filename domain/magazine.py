from domain.article import Article
from domain.article_collection import ArticleCollection


class Magazine:

    def __init__(self) -> None:
        self._articles = ArticleCollection()

    def publish_article(self, a_title, a_text):
        article = Article(a_title, a_text)
        import os
        if os.environ.get('TESTING_TECHNOLOGY') == 'PERFECT':
            return self._articles.add(article)
        if os.environ.get('TESTING_TECHNOLOGY') == 'DJANGO':
            from publishing_system.models import PersistentArticle

            return PersistentArticle.new_from(article)
        raise ValueError('Unknown Technology')

    def published_articles(self):
        return self._articles.all()

    def article_with_number(self, article_number):
        return self._articles.with_number(article_number)

    def _article_titles(self):
        return [article.title() for article in self._articles.all()]

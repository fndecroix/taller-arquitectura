from domain.article import Article
from domain.persistent_article_collection import PersistentArticleCollection
from domain.transient_article_collection import TransientArticleCollection


class Magazine:

    def __init__(self) -> None:
        self._articles = self._article_collection_for_technology()

    def _article_collection_for_technology(self):
        import os

        if os.environ.get('TESTING_TECHNOLOGY') == 'PERFECT':
            return TransientArticleCollection()
        elif os.environ.get('TESTING_TECHNOLOGY') == 'DJANGO':
            return PersistentArticleCollection()

        raise ValueError('Unknown technology')

    def publish_article(self, a_title, a_text):
        article = Article(a_title, a_text)
        return self._articles.add(article)

    def published_articles(self):
        return self._articles.all()

    def article_with_number(self, article_number):
        return self._articles.with_number(article_number)

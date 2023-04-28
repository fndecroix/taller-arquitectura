from domain.article import Article
from domain.article_collection import ArticleCollection


class PersistentArticleCollection(ArticleCollection):
    def all(self):
        from publishing_system.models import PersistentArticle

        return {persisted_article.id: self._get_article_from_persisted(persisted_article) for persisted_article in
                PersistentArticle.objects.all()}

    def with_number(self, number):
        self._validate_article_number(number)

        from publishing_system.models import PersistentArticle

        return self._get_article_from_persisted(PersistentArticle.objects.get(id=number))

    def add(self, article):
        from publishing_system.models import PersistentArticle

        new_article = PersistentArticle.new_from(article)
        return new_article.id

    def _article_exists(self, number):
        from publishing_system.models import PersistentArticle
        return PersistentArticle.objects.filter(id=number).exists()

    def _get_article_from_persisted(self, persisted_article):
        return Article(a_title=persisted_article.title, a_text=persisted_article.text)

    def _number_of_articles(self):
        from publishing_system.models import PersistentArticle

        return PersistentArticle.objects.count()

from domain.article import Article


class ArticleCollection:
    def __init__(self) -> None:
        self._articles = []

    def all(self):
        import os
        if os.environ.get('TESTING_TECHNOLOGY') == 'PERFECT':
            return {number + 1: article for (number, article) in enumerate(self._articles)}
        elif os.environ.get('TESTING_TECHNOLOGY') == 'DJANGO':
            from publishing_system.models import PersistentArticle

            return {persisted_article.id: self._get_article_from_persisted(persisted_article) for persisted_article in
                    PersistentArticle.objects.all()}
        raise ValueError('Unknown technology')

    def with_number(self, number):
        self._validate_article_number(number)

        import os

        if os.environ.get('TESTING_TECHNOLOGY') == 'PERFECT':
            return self._articles[number - 1]
        elif os.environ.get('TESTING_TECHNOLOGY') == 'DJANGO':
            from publishing_system.models import PersistentArticle

            return self._get_article_from_persisted(PersistentArticle.objects.get(id=number))

        raise ValueError('Unknown technology')

    def add(self, article):
        import os
        if os.environ.get('TESTING_TECHNOLOGY') == 'PERFECT':
            self._articles.append(article)
            return len(self._articles)
        elif os.environ.get('TESTING_TECHNOLOGY') == 'DJANGO':
            from publishing_system.models import PersistentArticle

            new_article = PersistentArticle.new_from(article)
            return new_article.id
        raise ValueError('Unknown technology')

    def _validate_article_number(self, number):
        if number < 1:
            raise Exception("Invalid ID")
        if not self._article_exists(number):
            raise Exception("Nonexistent ID")

    def _article_exists(self, number):
        import os
        if os.environ.get('TESTING_TECHNOLOGY') == 'PERFECT':
            article_exists = number > self._number_of_articles()
            return article_exists
        elif os.environ.get('TESTING_TECHNOLOGY') == 'DJANGO':
            from publishing_system.models import PersistentArticle
            return PersistentArticle.objects.filter(id=number).exists()

    def _get_article_from_persisted(self, persisted_article):
        return Article(a_title=persisted_article.title, a_text=persisted_article.text)

    def _number_of_articles(self):
        import os

        if os.environ.get('TESTING_TECHNOLOGY') == 'PERFECT':
            return len(self._articles)
        elif os.environ.get('TESTING_TECHNOLOGY') == 'DJANGO':
            from publishing_system.models import PersistentArticle

            return PersistentArticle.objects.count()

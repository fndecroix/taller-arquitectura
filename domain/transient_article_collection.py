from domain.article_collection import ArticleCollection


class TransientArticleCollection(ArticleCollection):
    def __init__(self) -> None:
        self._articles = []

    def all(self):
        return {number + 1: article for (number, article) in enumerate(self._articles)}

    def with_number(self, number):
        self._validate_article_number(number)

        return self._articles[number - 1]

    def add(self, article):
        self._articles.append(article)
        return len(self._articles)

    def _article_exists(self, number):
        return number > self._number_of_articles()

    def _number_of_articles(self):
        return len(self._articles)

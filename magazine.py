from article import Article


class Magazine:

    def __init__(self) -> None:
        self._articles = []

    def publish_article(self, a_title, a_text):
        self._validate_title(a_title)
        self._articles.append(Article(a_title, a_text))
        return len(self._articles)

    def published_articles(self):
        return self._articles

    def _validate_title(self, a_title):
        if a_title in self._article_titles():
            raise Exception('Cannot publish two articles with the same title')

    def _article_titles(self):
        return [article.title() for article in self._articles]

    def article_with_id(self, article_id):
        self._validate_article_id(article_id)
        return self._articles[article_id - 1]

    def _validate_article_id(self, article_id):
        if article_id > len(self._articles):
            raise Exception("Nonexistent ID")
        if len(self._articles) < 1:
            raise Exception("Invalid ID")

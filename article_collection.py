class ArticleCollection:
    def __init__(self) -> None:
        self._articles = []

    def all(self):
        return self._articles

    def with_number(self, number):
        self._validate_article_number(number)
        return self._articles[number - 1]

    def add(self, article):
        self._articles.append(article)
        return len(self._articles)

    def _validate_article_number(self, number):
        if number > len(self._articles):
            raise Exception("Nonexistent ID")
        if len(self._articles) < 1:
            raise Exception("Invalid ID")

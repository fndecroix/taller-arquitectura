class ArticleCollection:
    def all(self):
        raise NotImplementedError("Subclass responsibility")

    def with_number(self, number):
        raise NotImplementedError("Subclass responsibility")

    def add(self, article):
        raise NotImplementedError("Subclass responsibility")

    def _validate_article_number(self, number):
        if number < 1:
            raise Exception("Invalid ID")
        if not self._article_exists(number):
            raise Exception("Nonexistent ID")

    def _article_exists(self, number):
        raise NotImplementedError("Subclass responsibility")

    def _number_of_articles(self):
        raise NotImplementedError("Subclass responsibility")

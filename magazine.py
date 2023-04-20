class Magazine:

    def __init__(self) -> None:
        self._articles = []

    def publish_article(self, a_title, a_text):
        self._articles.append(Article(a_title, a_text))

    def published_articles(self):
        return self._articles


class Article:
    def __init__(self, a_title, a_text) -> None:
        self._validate_title(a_title)
        self._validate_text(a_text)
        self._title = a_title
        self._text = a_text

    def title(self):
        return self._title

    def text(self):
        return self._text

    def _validate_title(self, a_title):
        title_has_a_valid_length = 2 <= len(a_title) <= 50
        if not title_has_a_valid_length:
            raise Exception('The title must be 2 to 50 characters long')

    def _validate_text(self, a_text):
        text_has_a_valid_length = 1800 <= len(a_text) <= 5200
        if not text_has_a_valid_length:
            raise Exception('The text must be 1800 to 5200 characters long')

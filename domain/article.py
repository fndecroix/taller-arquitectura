class Article:
    MAX_TITLE_LENGTH = 50
    MIN_TITLE_LENGTH = 2
    MAX_TEXT_LENGTH = 5200
    MIN_TEXT_LENGTH = 5

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
        title_has_a_valid_length = self.MIN_TITLE_LENGTH <= len(a_title) <= self.MAX_TITLE_LENGTH
        if not title_has_a_valid_length:
            raise Exception('The title must be 2 to 50 characters long')

    def _validate_text(self, a_text):
        text_has_a_valid_length = self.MIN_TEXT_LENGTH <= len(a_text) <= self.MAX_TEXT_LENGTH
        if not text_has_a_valid_length:
            raise Exception('The text must be 1800 to 5200 characters long')

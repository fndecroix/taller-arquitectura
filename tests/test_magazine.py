from technology_test_case import TechnologyTestCase
from domain.magazine import Magazine
from tests.article_texts import ArticleTexts


class MagazineTest(TechnologyTestCase):
    def setUp(self) -> None:
        super().setUp()
        self._magazine = Magazine()

    def test_can_publish_an_article_to_a_magazine(self):
        self._magazine.publish_article(a_title=self._valid_title(), a_text=self._valid_text())

        self.assertEquals(1, len(self._magazine.published_articles()))

    def test_can_read_title_of_magazine_articles(self):
        article_title = self._valid_title()
        self._magazine.publish_article(a_title=article_title, a_text=self._valid_text())

        self._assert_article_has_title(1, article_title)

    def test_can_read_text_of_magazine_articles(self):
        article_title = self._valid_title()
        article_text = self._valid_text()
        self._magazine.publish_article(a_title=article_title, a_text=article_text)

        self._assert_article_has_text(1, article_text)

    def test_can_publish_multiple_articles_to_a_magazine(self):
        article_title = self._valid_title()
        article_text = self._valid_text()
        article_number = self._magazine.publish_article(a_title=article_title, a_text=article_text)
        other_article_title = 'other title'
        other_article_text = self._valid_text()

        other_article_number = self._magazine.publish_article(a_title=other_article_title, a_text=other_article_text)

        self._assert_article_has_title(other_article_number, other_article_title)
        self._assert_article_has_text(other_article_number, other_article_text)

    def test_cannot_publish_an_article_with_a_short_title(self):
        article_title = 'A'
        article_text = self._valid_text()
        expected_error_message = 'The title must be 2 to 50 characters long'
        self.assertRaisesWithMessage(expected_error_message, self._magazine.publish_article,
                                     **{'a_title': article_title, 'a_text': article_text})

    def test_cannot_publish_an_article_with_a_long_title(self):
        article_title = self._text_with_length(51)
        article_text = self._valid_text()
        expected_error_message = 'The title must be 2 to 50 characters long'
        self.assertRaisesWithMessage(expected_error_message, self._magazine.publish_article,
                                     **{'a_title': article_title, 'a_text': article_text})

    def test_cannot_publish_an_article_with_a_short_text(self):
        article_title = self._valid_title()
        article_text = self._text_with_length(1799)
        expected_error_message = 'The text must be 1800 to 5200 characters long'
        self.assertRaisesWithMessage(expected_error_message, self._magazine.publish_article,
                                     **{'a_title': article_title, 'a_text': article_text})

    def test_cannot_publish_an_article_with_a_long_text(self):
        article_title = self._valid_title()
        article_text = self._text_with_length(5201)
        expected_error_message = 'The text must be 1800 to 5200 characters long'
        self.assertRaisesWithMessage(expected_error_message, self._magazine.publish_article,
                                     **{'a_title': article_title, 'a_text': article_text})

    def test_cannot_access_an_article_by_a_nonexistent_id(self):
        article_nonexistent_id = 1

        expected_error_message = "Nonexistent ID"
        self.assertRaisesWithMessage(expected_error_message, self._magazine.article_with_number,
                                     **{'article_number': article_nonexistent_id})

    def test_cannot_access_an_article_by_an_invalid_id(self):
        article_invalid_id = -1

        expected_error_message = "Invalid ID"
        self.assertRaisesWithMessage(expected_error_message, self._magazine.article_with_number,
                                     **{'article_number': article_invalid_id})

    def _assert_article_has_text(self, article_number, article_text):
        self.assertEquals(article_text, self._magazine.article_with_number(article_number).text())

    # asserts

    def _assert_article_has_title(self, article_number, article_title):
        self.assertEquals(article_title, self._magazine.article_with_number(article_number).title())

    def assertRaisesWithMessage(self, error_message, closure, *args, **kwargs):
        try:
            closure(*args, **kwargs)
            self.fail()
        except Exception as error:
            self.assertEqual(str(error), error_message)

    # aux

    def _valid_text(self):
        return ArticleTexts().valid_text()

    def _valid_title(self):
        return ArticleTexts().valid_title()

    def _text_with_length(self, text_length):
        return ArticleTexts().text_with_length(text_length)

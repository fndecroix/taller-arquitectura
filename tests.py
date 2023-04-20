from unittest import TestCase

from magazine import Magazine


class MagazineTest(TestCase):
    def setUp(self) -> None:
        self._magazine = Magazine()

    def test_can_add_an_article_to_a_magazine(self):
        self._magazine.publish_article(a_title='A title', a_text=self._text_with_length(2000))

        self.assertEquals(1, len(self._magazine.published_articles()))

    def test_can_read_title_of_magazine_articles(self):
        article_title = 'A title'
        self._magazine.publish_article(a_title=article_title, a_text=self._text_with_length(2000))

        self._assert_article_has_title(0, article_title)

    def test_can_read_text_of_magazine_articles(self):
        article_title = 'A title'
        article_text = self._text_with_length(2000)
        self._magazine.publish_article(a_title=article_title, a_text=article_text)

        article_number = 0
        self._assert_article_has_text(article_number, article_text)

    def test_can_add_multiple_articles_to_a_magazine(self):
        article_title = 'A title'
        article_text = self._text_with_length(2000)
        self._magazine.publish_article(a_title=article_title, a_text=article_text)
        other_article_title = 'other title'
        other_article_text = self._text_with_length(2000)

        self._magazine.publish_article(a_title=other_article_title, a_text=other_article_text)

        self._assert_article_has_title(1, other_article_title)
        self._assert_article_has_text(1, other_article_text)

    def test_cannot_publish_an_article_with_a_short_title(self):
        article_title = 'A'
        article_text = self._text_with_length(2000)
        expected_error_message = 'The title must be 2 to 50 characters long'
        self.assertRaisesWithMessage(expected_error_message, self._magazine.publish_article,
                                     **{'a_title': article_title, 'a_text': article_text})

    def test_cannot_publish_an_article_with_a_long_title(self):
        article_title = self._text_with_length(51)
        article_text = self._text_with_length(2000)
        expected_error_message = 'The title must be 2 to 50 characters long'
        self.assertRaisesWithMessage(expected_error_message, self._magazine.publish_article,
                                     **{'a_title': article_title, 'a_text': article_text})

    def test_cannot_publish_an_article_with_a_short_text(self):
        article_title = 'A title'
        article_text = self._text_with_length(1799)
        expected_error_message = 'The text must be 1800 to 5200 characters long'
        self.assertRaisesWithMessage(expected_error_message, self._magazine.publish_article,
                                     **{'a_title': article_title, 'a_text': article_text})

    def test_cannot_publish_an_article_with_a_long_text(self):
        article_title = 'A title'
        article_text = self._text_with_length(5201)
        expected_error_message = 'The text must be 1800 to 5200 characters long'
        self.assertRaisesWithMessage(expected_error_message, self._magazine.publish_article,
                                     **{'a_title': article_title, 'a_text': article_text})

    # asserts

    def _assert_article_has_text(self, article_number, article_text):
        self.assertEquals(article_text, self._magazine.published_articles()[article_number].text())

    def _assert_article_has_title(self, article_number, article_title):
        self.assertEquals(article_title, self._magazine.published_articles()[article_number].title())

    def assertRaisesWithMessage(self, error_message, closure, *args, **kwargs):
        try:
            closure(*args, **kwargs)
            self.fail()
        except Exception as error:
            self.assertEqual(str(error), error_message)

    # aux

    def _text_with_length(self, text_length):
        return ''.join(['A' for i in range(0, text_length)])

from magazine import Magazine


class PublishingSystem:
    def __init__(self) -> None:
        self._magazine = Magazine()

    def published_articles(self):
        articles = self._magazine.published_articles()
        return [self._serialize_summarized_article(number, article) for number, article in articles.items()]

    def publish_article(self, a_title, a_text):
        return self._magazine.publish_article(a_title, a_text)

    def full_article(self, article_id):
        article = self._magazine.article_with_number(article_id)
        return self._serialize_full_article(article)

    def _serialize_summarized_article(self, number, article):
        return {
            'number': number,
            'text': article.text()[:100],
            'title': article.title()
        }
    def _serialize_full_article(self, article):
        return {
            'text': article.text(),
            'title': article.title()
        }

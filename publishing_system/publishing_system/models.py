from django.db import models

from domain.article import Article


class PersistentArticle(models.Model):
    title = models.TextField(max_length=Article.MAX_TITLE_LENGTH)
    text = models.TextField(max_length=Article.MAX_TEXT_LENGTH)

    @classmethod
    def new_from(cls, article):
        persistent_article = cls(title=article.title(), text=article.text())
        persistent_article.save()

from article_texts import ArticleTexts
from django_framework.xxx import Xxx
from system import PublishingSystem

Xxx().initialize_django_from_managepy(PublishingSystem())

from publishing_system.models import PersistentArticle
article = PersistentArticle(text=ArticleTexts().valid_text(), title=ArticleTexts().valid_title())
article.save()

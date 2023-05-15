class UrlConf:
    def __init__(self, system) -> None:
        self.system = system

    @property
    def urlpatterns(self):
        from django.urls import path

        from django_framework.publishing_system_views import PublishingSystemViews

        urlpatterns = [
            path('articles/', PublishingSystemViews(self.system).get_articles, name='list-articles'),
        ]

        return urlpatterns

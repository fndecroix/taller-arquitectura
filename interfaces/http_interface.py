import re


class HttpInterface:
    def __init__(self, publishing_system):
        self._publishing_system = publishing_system

    def get_article(self, request):
        article_number = request.parameters()['article_number']
        return HttpResponse(content=self._publishing_system.full_article(article_number))

    def get_articles(self, request):
        articles = self._publishing_system.published_articles()
        return HttpResponse(content=articles)


class HttpResponse:
    def __init__(self, content) -> None:
        self._content = content

    def content(self):
        return self._content


class HttpRequest:
    def __init__(self, parameters) -> None:
        self._parameters = parameters

    def parameters(self):
        return self._parameters

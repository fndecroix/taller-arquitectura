import re


class HttpInterface:
    def __init__(self, publishing_system):
        self._publishing_system = publishing_system

    def get_article(self, request):
        path = request.path()
        matches = re.match(r'/article/(?P<article_id>\d+)$', path)
        article_id = int(matches['article_id'][0])
        return HttpResponse(content=self._publishing_system.full_article(article_id))

    def get_articles(self, request):
        articles = self._publishing_system.published_articles()
        return HttpResponse(content=articles)


class HttpResponse:

    def __init__(self, content) -> None:
        self._content = content

    def content(self):
        return self._content


class HttpRequest:

    def __init__(self, path) -> None:
        self._path = path

    def path(self):
        return self._path

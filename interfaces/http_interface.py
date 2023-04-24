import re


class HttpInterface:
    def __init__(self, publishing_system):
        self._publishing_system = publishing_system

    def get(self, request):
        path = request['path']
        if path == '/articles':
            articles = self._publishing_system.published_articles()
            return HttpResponse(content=articles)
        else:
            matches = re.match(r'/article/(?P<article_id>\d+)$', path)
            article_id = int(matches['article_id'][0])
            return HttpResponse(content=self._publishing_system.full_article(article_id))


class HttpResponse:

    def __init__(self, content) -> None:
        self._content = content

    def content(self):
        return self._content

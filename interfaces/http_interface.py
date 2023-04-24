class HttpInterface:
    def __init__(self, publishing_system):
        self._publishing_system = publishing_system

    def get(self, path):
        articles = self._publishing_system.published_articles()
        return HttpResponse(content=articles)


class HttpResponse:

    def __init__(self, content) -> None:
        self._content = content

    def content(self):
        return self._content

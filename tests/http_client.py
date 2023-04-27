from interfaces.http_interface import HttpRequest, HttpInterface


class HttpClient:
    def __init__(self) -> None:
        self.publishing_system = None

    def get_articles(self):
        return self.interface().get_articles(self._http_request_with(parameters={}))

    def get_article(self, article_number):
        parameters = {'article_number': article_number}
        return self.interface().get_article(self._http_request_with(parameters=parameters))

    def set_system(self, new_system):
        self.publishing_system = new_system

    def interface(self):
        return HttpInterface(self.publishing_system)

    def _http_request_with(self, parameters):
        return HttpRequest(parameters=parameters)

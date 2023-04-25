from interfaces.http_interface import HttpRequest


class HttpClient:
    def __init__(self, interface) -> None:
        self._interface = interface

    def get_articles(self):
        return self._interface.get_articles(self._http_request_with(parameters={})).content()

    def get_article(self, article_number):
        parameters = {'article_number': article_number}
        return self._interface.get_article(self._http_request_with(parameters=parameters)).content()

    def _http_request_with(self, parameters):
        return HttpRequest(parameters=parameters)

import json

from django.http import HttpResponse


class DjangoHttpResponse:
    @classmethod
    def response_for(cls, response):
        return HttpResponse(content=json.dumps(response.content()))

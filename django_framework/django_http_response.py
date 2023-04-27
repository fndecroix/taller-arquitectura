import json


class DjangoHttpResponse:
    @classmethod
    def response_for(cls, response):
        from django.http import HttpResponse

        return HttpResponse(content=json.dumps(response.content()))

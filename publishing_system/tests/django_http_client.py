import json

from django.urls import reverse


class DjangoHttpClient:
    def __init__(self, testcase) -> None:
        self.testcase = testcase

    def get_articles(self):
        django_response = self.testcase.client.get(reverse('list-articles'))
        return json.loads(django_response.content)

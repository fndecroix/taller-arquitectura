import json

from django.test.client import Client
from django.urls import reverse

from publishing_system.publishing_system.global_publishing_system import GlobalPublishingSystem


class DjangoHttpClient:
    def set_system(self, new_system):
        GlobalPublishingSystem.set_system(new_system)

    def get_articles(self):
        django_response = self.django_client().get(reverse('list-articles'))
        return json.loads(django_response.content)

    def django_client(self):
        return Client()

import io
from unittest import TestCase

from interfaces.command_line_interface import CommandLineInterface
from system import PublishingSystem
from tests.article_texts import ArticleTexts


class CommandLineInterfaceTest(TestCase):
    def setUp(self):
        self.output_stream = io.StringIO()
        self.publishing_system = PublishingSystem()
        self.interface = self._interface_with_input(self.output_stream)

    def test_when_an_article_is_published_the_operation_is_successful(self):
        operations = [
            {
                'operation': 'publish',
                'title': ArticleTexts().valid_title(),
                'text': ArticleTexts().valid_text(),
             },
        ]

        self.interface.process(operations[0])

        expected_text = f'Published article: {operations[0]["title"]}'
        output_message = self._get_message_from_output(self.output_stream)

        self.assertEquals(output_message, expected_text)
        self.assertEquals(len(self.publishing_system.published_articles()), 1)

    def _interface_with_input(self, output_stream):
        return CommandLineInterface(publishing_system=self.publishing_system,
                                    output_stream=output_stream)

    def _get_message_from_output(self, output_stream):
        output_stream.seek(0)
        return output_stream.read()


from django.core.management.base import BaseCommand

from system import PublishingSystem


class Command(BaseCommand):
    help = "Publish an article in the Django magazine"

    def add_arguments(self, parser):
        parser.add_argument('title', type=str)
        parser.add_argument('text', type=str)

    def handle(self, *args, **options):
        import sys
        from interfaces.command_line_interface import CommandLineInterface
        system = PublishingSystem()
        interface = CommandLineInterface(system, sys.stdout)

        interface.publish_article(options)

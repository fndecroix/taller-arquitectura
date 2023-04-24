class CommandLineInterface:
    def __init__(self, publishing_system, output_stream) -> None:
        self._publishing_system = publishing_system
        self._output_stream = output_stream

    def publish_article(self, operation):
        article_id = self._publishing_system.publish_article(operation["title"], operation["text"])
        self._output_stream.write(f'Published article {article_id}: {operation["title"]}')

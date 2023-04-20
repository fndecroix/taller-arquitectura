class ArticleTexts:
    def text_with_length(self, text_length):
        return ''.join(['A' for i in range(0, text_length)])

    def valid_text(self):
        return self.text_with_length(2000)

    def summarized_text_for(self, full_text):
        return full_text[:100]

    def valid_title(self):
        return 'A title'

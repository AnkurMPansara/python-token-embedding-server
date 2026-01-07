from .textToVector import TextToVector

class EmbedText:
    def __init__(self):
        self.embedder = TextToVector()

    def get_embedding(self, text: str):
        return self.embedder.embed_text(text)

# Singleton instance
embedTextInstance = EmbedText()

import gensim.downloader as api
import numpy as np
import threading

class TextToVector:
    def __init__(self):
        self.model = None
        self.ready = False
        threading.Thread(target=self._load_model, daemon=True).start()

    def _load_model(self):
        print("Loading Word2Vec model in background...")
        self.model = api.load("word2vec-google-news-300")  # can swap with FastText
        self.ready = True
        print("Model loaded!")

    def embed_text(self, text: str):
        if not self.ready:
            return None
        words = text.split()
        vectors = [self.model[word] for word in words if word in self.model]
        if not vectors:
            return []
        return np.mean(vectors, axis=0).tolist()

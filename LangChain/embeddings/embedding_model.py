from sentence_transformers import SentenceTransformer

class CustomEmbedding:
    def __init__(self):
        model = SentenceTransformer('all-MiniLM-L6-v2')
        self.model = model

    def embed_query(self, text):
        return self.model.encode(text).tolist()

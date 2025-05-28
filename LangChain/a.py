from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

text = "Hola, ¿cómo estás?"
embedding = model.encode(text)

print(f"Vector embedding para '{text}':")
print(embedding)
print(f"Tamaño vector: {embedding.shape}")

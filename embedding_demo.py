from dotenv import load_dotenv
from google import genai
import os
import numpy as np

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

sentences = [
    "I love learning artificial intelligence.",
    "I enjoy studying AI and machine learning.",
    "The weather is very cold today."
]

result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=sentences
)

embeddings = [item.values for item in result.embeddings]

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)

    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

similarity_ab = cosine_similarity(embeddings[0], embeddings[1])
similarity_ac = cosine_similarity(embeddings[0], embeddings[2])

print("A vs B:", similarity_ab)
print("A vs C:", similarity_ac)
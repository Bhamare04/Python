from google import genai
from dotenv import load_dotenv
import os
import chromadb

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

chroma_client = chromadb.PersistentClient(
    path="./chromadb"
)

collection = chroma_client.get_collection(
    name="knowledge_collection"
)

question = "How many paid leaves do employees get?"

# Convert question into embedding
result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=question
)

query_embedding = result.embeddings[0].values

# Search ChromaDB
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=1
)

print("\nUser Question:")
print(question)

print("\nRetrieved Documents:")

for document in results["documents"][0]:
    print("-", document)

# Combine retrieved documents
context = "\n\n".join(results["documents"][0])

# Create prompt
prompt = f"""
Answer the user's question using only the provided context.

Context:
{context}

Question:
{question}

If the answer is not present in the context, say:
"I don't have enough information in the provided documents."
"""

# Generate final answer
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt
)

print("\nGenerated Response:")
print(response.text)
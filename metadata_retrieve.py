from google import genai
from dotenv import load_dotenv
import chromadb
import os

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(
    api_key=api_key
)

# Connect to ChromaDB
chroma_client = chromadb.PersistentClient(
    path="./chromadb"
)

collection = chroma_client.get_collection(
    name="knowledge_metadata"
)

# Check collection
print("Collection count:", collection.count())

# Check stored data
stored_data = collection.get()

print("\nStored IDs:")
print(stored_data["ids"])

print("\nStored Documents:")
print(stored_data["documents"])

print("\nStored Metadata:")
print(stored_data["metadatas"])


# User question
question = "how many paid leaves do employees get?"

print("\nUser Question:")
print(question)


# Create query embedding
result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=question
)

query_embedding = result.embeddings[0].values


# Search WITHOUT metadata filter first
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=2,
    where={
        "$and":#$or
        [
            {"department":"HR"},
            {"year":2026}
        ]
    }
)

print("\nRetrieved Results:")
print(results)


# Print documents
if results["documents"] and results["documents"][0]:

    for i, document in enumerate(results["documents"][0]):

        print(f"\nChunk {i + 1}")
        print("Document:", document)

        if results["metadatas"]:
            print(
                "Metadata:",
                results["metadatas"][0][i]
            )

        if results["distances"]:
            print(
                "Distance:",
                results["distances"][0][i]
            )

else:

    print("\nNo documents were retrieved.")
### `rag_threshold.py`

from google import genai
from dotenv import load_dotenv
import chromadb
import os

# --------------------------------------------------
# 1. Load environment variables
# --------------------------------------------------

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(
    api_key=api_key
)

# --------------------------------------------------
# 2. Connect to persistent ChromaDB
# --------------------------------------------------

chroma_client = chromadb.PersistentClient(
    path="./chromadb"
)

collection = chroma_client.get_collection(
    name="knowledge_collection"
)

# --------------------------------------------------
# 3. User question
# --------------------------------------------------

question = "How many paid leaves do employees get?"

print("\nUser Question:")
print(question)

# --------------------------------------------------
# 4. Convert question into embedding
# --------------------------------------------------

result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=question
)

query_embedding = result.embeddings[0].values

# --------------------------------------------------
# 5. Search ChromaDB
# --------------------------------------------------

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3
)

# --------------------------------------------------
# 6. Display retrieved chunks and distances
# --------------------------------------------------

print("\nRetrieved Chunks:")

documents = results["documents"][0]
distances = results["distances"][0]

for i, document in enumerate(documents):

    print(f"\nChunk {i + 1}")
    print("Distance:", distances[i])
    print("Document:", document)

# --------------------------------------------------
# 7. Similarity threshold
# --------------------------------------------------

threshold = 0.7

print("\n" + "=" * 50)
print("Applying Similarity Threshold:", threshold)
print("=" * 50)

relevant_documents = []

for i, document in enumerate(documents):

    distance = distances[i]

    # Lower distance = more similar
    if distance <= threshold:

        relevant_documents.append(document)

        print("\nRelevant Chunk:")
        print("Distance:", distance)
        print("Document:", document)

# --------------------------------------------------
# 8. Check whether relevant information exists
# --------------------------------------------------

if not relevant_documents:

    print("\nNo sufficiently relevant documents found.")

else:

    print("\nTotal Relevant Chunks:",
          len(relevant_documents))

# # --------------------------------------------------
# # 9. Create context for LLM
# # --------------------------------------------------

# if relevant_documents:

#     context = "\n\n".join(relevant_documents)

#     prompt = f"""
# Answer the user's question using ONLY the provided context.

# Context:
# {context}

# Question:
# {question}

# Rules:
# - Use only the provided context.
# - Do not make up information.
# - If the answer is not present in the context, say:
# "I don't have enough information in the provided documents."
# """

#     # --------------------------------------------------
#     # 10. Generate final answer
#     # --------------------------------------------------

#     print("\nSending context to Gemini...")

#     response = client.models.generate_content(
#         model="gemini-3.8-flash",
#         contents=prompt
#     )

#     print("\nGenerated Answer:")
#     print(response.text)

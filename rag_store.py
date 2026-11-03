from google import genai
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(
    api_key=api_key
)

# Read document
with open("knowledge.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Split document
splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20
)

chunks = splitter.split_text(text)

print("Number of chunks:", len(chunks))

# ChromaDB
chroma_client = chromadb.PersistentClient(
    path="./chromadb"
)

collection = chroma_client.get_or_create_collection(
    name="knowledge_metadata"
)

# Create embeddings
result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=chunks
)

embeddings = [
    item.values
    for item in result.embeddings
]

# Create metadata
metadatas = []

for i in range(len(chunks)):

    metadatas.append({
        "category": "company_policy",
        "department": "HR",
        "year": 2026
    })

# Store everything
collection.add(
    ids=[f"chunk_{i}" for i in range(len(chunks))],
    documents=chunks,
    embeddings=embeddings,
    metadatas=metadatas
)

print("Documents stored successfully!")

print("Number of documents:",
      collection.count())
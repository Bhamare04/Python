from google import genai
from dotenv import load_dotenv
import os 
import chromadb


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

chroma_client = chromadb.PersistentClient(
    path ="./chromadb"
)

collection = chroma_client.get_collection(
    name = "knowledge_collection"
)

question = "how many paid leaves do employees get?"

result = client.models.embed_content(
    model = "gemini-embedding-001",
    contents = question
)

query_embedding = result.embeddings[0].values

#search chromadb
results = collection.query(
    query_embeddings=[query_embedding],
    n_results = 1
)
print("\n user question:")
print(question)

print("retrieved documnets")

for document in results["documents"][0]:
    print("-",document)
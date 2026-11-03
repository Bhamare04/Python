import chromadb
#create a client

client = chromadb.Client()

#creayte a collection
collection = client.create_collection(name="my_collection")

# Documents we want to store
documents = [
    "I love learning artificial intelligence.",
    "I enjoy studying machine learning and deep learning.",
    "Python is a popular programming language.",
    "The weather is very cold today."
]

#add documents to the collection
collection.add(
    documents=documents,
    ids=["doc1", "doc2", "doc3", "doc4"]
)

# print("Documents added to the collection.")
# print("Collection name:", collection.count())

#search for similar documents
query = "I want to learn AI"

results = collection.query(
    query_texts=[query],
    n_results=2
)

for document in results["documents"][0]:
    print("-",document)

print(collection.get())
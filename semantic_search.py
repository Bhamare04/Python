from google import genai
from dotenv import load_dotenv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os


# ============================================================
# 1. LOAD GEMINI API
# ============================================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


# ============================================================
# 2. DOCUMENTS AND QUERY
# ============================================================

documents = [
    "Employees are entitled to 20 paid leaves per year.",
    "Employees must apply for planned leave 3 days in advance.",
    "Employees can work from home up to 2 days per week.",
    "Python is a popular programming language."
]

query = "How many paid leaves do employees get?"


# ============================================================
# 3. TF-IDF KEYWORD SEARCH
# ============================================================

vectorizer = TfidfVectorizer()

# Convert documents into TF-IDF vectors
document_vectors = vectorizer.fit_transform(documents)

# Convert query into TF-IDF vector
query_vector = vectorizer.transform([query])

# Calculate TF-IDF similarity
tfidf_similarities = cosine_similarity(
    query_vector,
    document_vectors
)

tfidf_scores = tfidf_similarities[0]

print("\nTF-IDF Scores:")

for i, score in enumerate(tfidf_scores):
    print(f"Document {i + 1}: {score:.4f}")


# ============================================================
# 4. GEMINI SEMANTIC SEARCH
# ============================================================

# Create embeddings for documents
result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=documents
)

embeddings = [
    item.values
    for item in result.embeddings
]

print("\nNumber of embeddings:", len(embeddings))
print("Dimensions:", len(embeddings[0]))


# Create embedding for query
query_result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=query
)

query_embedding = query_result.embeddings[0].values

print(
    "Query embedding dimensions:",
    len(query_embedding)
)


# Calculate semantic similarity
semantic_similarities = cosine_similarity(
    [query_embedding],
    embeddings
)

semantic_scores = semantic_similarities[0]

print("\nSemantic Scores:")

for i, score in enumerate(semantic_scores):
    print(f"Document {i + 1}: {score:.4f}")


# ============================================================
# 5. MIN-MAX NORMALIZATION FUNCTION
# ============================================================

def min_max_normalize(scores):

    min_score = min(scores)
    max_score = max(scores)

    # Prevent division by zero
    if max_score == min_score:
        return [1.0 for _ in scores]

    return [
        (score - min_score) / (max_score - min_score)
        for score in scores
    ]


# ============================================================
# 6. NORMALIZE TF-IDF SCORES
# ============================================================

normalized_tfidf = np.array(
    min_max_normalize(tfidf_scores)
)

print("\nNormalized TF-IDF Scores:")

for i, score in enumerate(normalized_tfidf):
    print(f"Document {i + 1}: {score:.4f}")


# ============================================================
# 7. NORMALIZE SEMANTIC SCORES
# ============================================================

normalized_semantic = np.array(
    min_max_normalize(semantic_scores)
)

print("\nNormalized Semantic Scores:")

for i, score in enumerate(normalized_semantic):
    print(f"Document {i + 1}: {score:.4f}")


# ============================================================
# 8. CALCULATE HYBRID SCORE
# ============================================================

# 30% keyword relevance
# 70% semantic relevance

hybrid_scores = (
    0.3 * normalized_tfidf
    + 0.7 * normalized_semantic
)


print("\nHybrid Scores:")

for i, score in enumerate(hybrid_scores):
    print(f"Document {i + 1}: {score:.4f}")


document_scores = list(zip(documents,hybrid_scores))

ranked_documents = sorted(
    document_scores,
    key = lambda x : x[1],
    reverse = True
)

top_k = 2
print(f"\nTop {top_k} Documents based on Hybrid Scores:")

for document,score in ranked_documents[:top_k]:
    print(f"Document: {document}")
    print(f"Hybrid Score: {score:.4f}\n")
    print()
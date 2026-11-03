from sklearn.feature_extraction.text import TfidfVectorizer

#TF-IDF : Term-frequency , Inverse document frequency                       How important is each word?  
#TF-IDF is a numerical statistic that reflects how important a word is to a document in a collection or corpus.
#\[
#IDF(t)=\log\left(\frac{N}{DF(t)}\right)
#\]

from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "Employees are entitled to 20 paid leaves per year.",
    "Employees must apply for planned leave 3 days in advance.",
    "Employees can work from home up to 2 days per week.",
    "Python is a popular programming language."
]

query = "how many paid leaves do employees get?"


vectorizer = TfidfVectorizer()



document_vectors = vectorizer.fit_transform(documents)

query_vector = vectorizer.transform([query])

print("Document vectors:")
print(document_vectors)

print("\nQuery vector:")
print(query_vector)


def min_max_normalize(scores):
    min_score = min(scores)
    max_score = max(scores)

    if max_score == min_score:
        return [1.0 for _ in scores]

    return [
        (score - min_score) / (max_score - min_score)
        for score in scores
    ]
tfidf_similarities = cosine_similarity(
    query_vector,
    document_vectors
)

tfidf_scores = tfidf_similarities[0]

normalized_tfidf = min_max_normalize(tfidf_scores)

print("\nNormalized TF-IDF Scores:")

for i, score in enumerate(normalized_tfidf):
    print(f"Document {i + 1}: {score:.4f}")
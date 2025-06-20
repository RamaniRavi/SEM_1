# 2.1 Vector-Based Ranking (22 Points)

# Given the following documents:
    # d0 = “learning vector representation classification”
    # d1 = “probabilistic inference language model”
    # d2 = “vector space model for retrieval”

# and the Query:
    # q = “vector model retrieval”



from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

# Define the documents and the query
documents = [
    "learning vector representation classification",  # d0
    "probabilistic inference language model",          # d1
    "vector space model for retrieval"                 # d2
]
query = ["vector model retrieval"]


# ===================================================================

# 2.1.1 TF-IDF (8.8 Points)
    # Compute the TF-IDF vectors for each document and the query. Each right answer scores 0.2 points.
    # Note: Give the numerical answers rounded to three decimal places, e.g., 0.185. Round the last digit as follows: 0.1856 → 0.186, 0.1851 → 0.185, 0.1855 → 0.186, 0→ 0.0

# --->
# Combine documents and query for consistent TF-IDF vectorization
corpus = documents + query

# Create a TF-IDF vectorizer with simple tokenization
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(corpus)
feature_names = vectorizer.get_feature_names_out()

# Convert to a dense matrix and create a DataFrame for display
tfidf_dense = tfidf_matrix.toarray()
tfidf_df = pd.DataFrame(tfidf_dense, columns=feature_names, index=['d0', 'd1', 'd2', 'query'])

# Reorder the columns as per the question order
terms_order = [
    "classification", "for", "inference", "language", "learning",
    "model", "probabilistic", "representation", "retrieval", "space", "vector"
]

# Round to 3 decimal places as specified
result_df = tfidf_df[terms_order].round(3)
result_df.T  # Transpose to match the question format (terms as rows)
print(result_df)

# =================================================================
# 2.1.2 Cosine Similarity Scores (12 Points)
    # Compute cosine similarity scores between the query and each document. Each right answer scores 4 points. No negative points are deducted for wrong answers.
    # Note: Give the numerical answers rounded to two decimal places, e.g., 0.18. Round the last digit as follows: 0.182 → 0.18,  0.185 → 0.19, 0.186 → 0.19

# --->
# Compute cosine similarities between the query and each document
# Note: query is the last row in tfidf_df (index 3)
cosine_similarities = cosine_similarity(tfidf_dense[:-1], tfidf_dense[-1].reshape(1, -1)).flatten()

# Round to 2 decimal places as specified
cosine_sim_rounded = np.round(cosine_similarities, 2)
print(cosine_sim_rounded)

# =========================================================================
# 2.1.3 Document Ranking (1.2 Points)
    # Rank the documents by similarity. Which document has the highest rank? 

# --->
# Based on the cosine similarity scores:
# d2: 0.65
# d0: 0.18
# d1: 0.18

# The document with the highest rank is: d2
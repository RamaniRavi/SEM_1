from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np

# Define the documents and the query
documents = [
    "learning vector representation classification",  # d0
    "probabilistic inference language model",          # d1
    "vector space model for retrieval"                 # d2
]
query = ["vector model retrieval"]

# Compute cosine similarities between the query and each document
# Note: query is the last row in tfidf_df (index 3)
cosine_similarities = cosine_similarity(tfidf_dense[:-1], tfidf_dense[-1].reshape(1, -1)).flatten()

# Round to 2 decimal places as specified
cosine_sim_rounded = np.round(cosine_similarities, 2)
cosine_sim_rounded

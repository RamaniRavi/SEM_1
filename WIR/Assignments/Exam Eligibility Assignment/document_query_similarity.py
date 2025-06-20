import pandas as pd
import numpy as np
corpus = [
    "sum sum",
    "cloud wind wind rain rain",
    "sum cloud cloud wind",
    "sum sum sum cloud cloud wind wind wind rain",
    "wind wind snow snow"
]
query = "cloud wind"
vocabulary = ['sum', 'cloud', 'wind', 'rain', 'snow']

def build_tf_matrix(corpus, vocabulary):
    tf_matrix = []
    for doc in corpus:
        words = doc.split()
        tf_vector = [words.count(term) for term in vocabulary]
        tf_matrix.append(tf_vector)
    return pd.DataFrame(tf_matrix, columns=vocabulary)

tf_matrix = build_tf_matrix(corpus, vocabulary)

def compute_idf(tf_matrix):
    N = len(tf_matrix)
    df = (tf_matrix > 0).sum(axis=0)
    idf = np.log(N / df)
    return idf

idf_vector = compute_idf(tf_matrix)
tfidf_matrix = tf_matrix * idf_vector

def build_query_vector(query, vocabulary, idf_vector):
    words = query.split()
    tf = pd.Series([words.count(term) for term in vocabulary], index=vocabulary)
    return tf * idf_vector

query_vector = build_query_vector(query, vocabulary, idf_vector)

def cosine_similarity(tfidf_matrix, query_vector):
    similarities = {}
    q_vec = query_vector.to_numpy()
    q_norm = np.linalg.norm(q_vec)
    for i, doc_vector in tfidf_matrix.iterrows():
        d_vec = doc_vector.to_numpy()
        d_norm = np.linalg.norm(d_vec)
        dot_product = np.dot(q_vec, d_vec)
        sim = dot_product / (q_norm * d_norm) if q_norm > 0 and d_norm > 0 else 0
        similarities[f'd{i+1}'] = sim
    return similarities

similarities = cosine_similarity(tfidf_matrix, query_vector)
print("TF-IDF Cosine Similarities:", similarities)
print(tfidf_matrix)
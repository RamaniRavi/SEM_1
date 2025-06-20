from collections import Counter
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_term_probabilities(documents):
    corpus_terms = []
    doc_term_freqs = []
    doc_lengths = []
    
    for doc in documents:
        terms = doc.split()
        corpus_terms.extend(terms)
        counter = Counter(terms)
        doc_term_freqs.append(counter)
        doc_lengths.append(len(terms))
    
    corpus_counter = Counter(corpus_terms)
    corpus_length = len(corpus_terms)
    
    doc_term_probs = []
    for i, counter in enumerate(doc_term_freqs):
        length = doc_lengths[i]
        prob_dict = {term: freq/length for term, freq in counter.items()}
        doc_term_probs.append(prob_dict)
    
    corpus_term_probs = {term: freq/corpus_length for term, freq in corpus_counter.items()}
    
    return doc_term_probs, corpus_term_probs

def query_likelihood_unigram(query_terms, doc_term_probs, doc_lengths, doc_index):
    prob = 1.0
    doc_prob_dict = doc_term_probs[doc_index]
    length = doc_lengths[doc_index]
    for t in query_terms:
        pt = doc_prob_dict.get(t, 0)
        prob *= pt
    return prob

def query_likelihood_interpolated(query_terms, doc_term_probs, corpus_term_probs, doc_lengths, doc_index, lam=0.5):
    prob = 1.0
    doc_prob_dict = doc_term_probs[doc_index]
    length = doc_lengths[doc_index]
    for t in query_terms:
        p_doc = doc_prob_dict.get(t, 0)
        p_corp = corpus_term_probs.get(t, 0)
        p = lam * p_doc + (1 - lam) * p_corp
        prob *= p
    return prob

corpus = [
    "vaccine research corona virus research",
    "research research cancer vaccine vaccine",
    "virus virus corona vaccine lab",
    "cancer lab research lab"
]

doc_term_probs, corpus_term_probs = compute_term_probabilities(corpus)
doc_lengths = [len(doc.split()) for doc in corpus]

query = "research vaccine".split()

print("Query Likelihood Unsmoothed Model Probabilities:")
for i in range(len(corpus)):
    prob = query_likelihood_unigram(query, doc_term_probs, doc_lengths, i)
    print(f"d{i+1}: {prob}")

print("\nQuery Likelihood Interpolated Model Probabilities (λ=0.7):")
lam = 0.7
for i in range(len(corpus)):
    prob = query_likelihood_interpolated(query, doc_term_probs, corpus_term_probs, doc_lengths, i, lam)
    print(f"d{i+1}: {prob}")

documents = [
    "The sky is blue and beautiful.",
    "Love this blue and beautiful sky!",
    "The quick brown fox jumps over the lazy dog.",
    "A king's breakfast has sausages, ham, bacon, eggs, toast, and beans",
    "I love green eggs, ham, sausages and bacon!",
    "The brown fox is quick and the blue dog is lazy!",
    "The sky is very blue and the sky is very beautiful today",
    "The dog is lazy but the brown fox is quick!"
]

query = ["quick brown fox"]

vectorizer = TfidfVectorizer()

tfidf_docs = vectorizer.fit_transform(documents)

tfidf_query = vectorizer.transform(query)

cos_similarities = cosine_similarity(tfidf_query, tfidf_docs).flatten()

ranked_doc_indices = np.argsort(-cos_similarities)

print("\nDocuments ranked by relevance to query:")
for rank, idx in enumerate(ranked_doc_indices, 1):
    print(f"{rank}. Doc{idx+1} (score: {cos_similarities[idx]:.4f}): {documents[idx]}")
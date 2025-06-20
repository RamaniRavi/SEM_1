# 2.2 Query Likelihood Scoring (18 Points)

# You are given a document:
# d1 = "deep learning improves natural language understanding in many applications"

# And a query:
# q = "language applications"

# If we assume the document itself is the collection, compute the query likelihood score:
# ==============================================================================================

from collections import Counter
from nltk.util import bigrams

# Document and Query
document = "deep learning improves natural language understanding in many applications"
query = "language applications"

# Tokenize the document and query
doc_tokens = document.lower().split()
query_tokens = query.lower().split()

# Unigram model (MLE)
doc_counts = Counter(doc_tokens)
doc_length = len(doc_tokens)

# --------------------------------------------------------------------------------------
# 2.2.1 Maximum Likelihood Estimation (6 Points)

# Under a unigram language model using Maximum Likelihood Estimation (MLE): # 0.012
# Under a diagram language model using Maximum Likelihood Estimation (MLE): # 0.0
# Note: Give the numerical answers rounded to three decimal places, e.g., 0.185. Round the last digit as follows: 0.1856 → 0.186, 0.1851 → 0.185, 0.1855 → 0.186, 0→ 0.0
# --->
unigram_likelihood = 1.0
for word in query_tokens:
    word_count = doc_counts.get(word, 0)
    prob = word_count / doc_length
    unigram_likelihood *= prob

# Bigram model (MLE)
bigram_counts = Counter(bigrams(doc_tokens))
bigram_likelihood = 1.0

for i in range(len(query_tokens) - 1):
    prev_word = query_tokens[i]
    curr_word = query_tokens[i + 1]
    bigram = (prev_word, curr_word)

    bigram_count = bigram_counts.get(bigram, 0)
    unigram_count = doc_counts.get(prev_word, 0)

    if unigram_count == 0:
        bigram_likelihood = 0.0
        break

    prob = bigram_count / unigram_count
    bigram_likelihood *= prob

# Print results
print("Unigram Query Likelihood Score (MLE):", round(unigram_likelihood, 3))
print("Bigram Query Likelihood Score (MLE):", round(bigram_likelihood, 3))


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 2.2.2 Laplace Smoothing (6 Points)
# Under a unigram language model using Laplace smoothing (use '1' in the Laplace formula for alpha): # 0.012

# Note: Give the numerical answers rounded to three decimal places, e.g., 0.185. Round the last digit as follows: 0.1856 → 0.186, 0.1851 → 0.185, 0.1855 → 0.186, 0→ 0.0
# ---->

vocab_size = len(set(doc_tokens))

# Laplace smoothing
alpha = 1
laplace_likelihood = 1.0

for word in query_tokens:
    count = doc_counts.get(word, 0)
    prob = (count + alpha) / (doc_length + vocab_size)
    laplace_likelihood *= prob

print("Unigram Query Likelihood Score (Laplace Smoothing):", round(laplace_likelihood, 3))

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 2.2.3 Jelinek-Mercer Smoothing (6 Points)
# Under a unigram language model using Jelinek-Mercer smoothing (λ = 0.8, use uniform background model): # 0.012

# Note: # A uniform background model assumes that every term in the vocabulary has equal probability in the global collection: p(w/c) = 1/|v|
# for all w in the vocabulary V.
# Also: Give the numerical answers rounded to three decimal places, e.g., 0.185. Round the last digit as follows: 0.1856 → 0.186, 0.1851 → 0.185, 0.1855 → 0.186, 0→ 0.0
# ----->

vocab = set(doc_tokens)
vocab_size = len(vocab)

# Smoothing parameter
lam = 0.8
uniform_prob = 1 / vocab_size

jm_likelihood = 1.0

for word in query_tokens:
    mle = doc_counts.get(word, 0) / doc_length
    smoothed_prob = lam * mle + (1 - lam) * uniform_prob
    jm_likelihood *= smoothed_prob

print("Unigram Query Likelihood Score (Jelinek-Mercer Smoothing):", round(jm_likelihood, 3))
def Rocchio(alpha, beta, gamma):
    d0 = "king palace jungle sleeps".split()
    d1 = "jungle lion fire king discovery".split()
    d2 = "king timon musafa".split()
    d3 = "timon lion simba".split()
    q = "lion king".split()

    # Create the word bag (unique sorted list of words)
    word_bag = sorted(set(d0 + d1 + d2 + d3 + q))

    # Create binary vectors for query, relevant doc, and irrelevant doc
    def vectorize(doc):
        return [1 if word in doc else 0 for word in word_bag]

    q_vec = vectorize(q)
    d1_vec = vectorize(d1)  # relevant
    d3_vec = vectorize(d3)  # irrelevant

    # Calculate Rocchio feedback vector
    q_prime = []
    for i in range(len(word_bag)):
        val = alpha * q_vec[i] + beta * d1_vec[i] - gamma * d3_vec[i]
        q_prime.append(round(val, 2))

    # Return results as dict word: score
    return dict(zip(word_bag, q_prime))

# Calculate Rocchio feedback with given parameters
result = Rocchio(alpha=1, beta=0.1, gamma=0.9)

# Display relevant words asked
words_to_show = ['fire', 'timon', 'discovery', 'sleeps', 'lion', 'king', 'jungle', 'simba', 'mufasa', 'palace']
for word in words_to_show:
    print(f"{word:<10} {result[word]}")

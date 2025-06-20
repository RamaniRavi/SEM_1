import numpy as np

d0 = "king palace jungle sleeps".split()
d1 = "jungle lion fire king discovery".split()
d2 = "king timon musafa".split()
d3 = "timon lion simba".split()
q = "lion king".split()

word_bag = list(set(d0 + d1 + d2 + d3 + q))
word_bag.sort()

print(word_bag)
      
alpha = 1
beta = 0.8
gamma = 0.1

# Vectors based on word_bag
q =        np.array([0, 0, 0, 1, 1, 0, 0, 0, 0, 0])
d1 =       np.array([1, 1, 1, 1, 1, 0, 0, 0, 0, 0])  # relevant
d3 =       np.array([0, 0, 0, 0, 1, 0, 0, 1, 0, 1])  # irrelevant

# Apply Rocchio formula
q_prime = alpha * q + beta * d1 - gamma * d3
q_prime = np.round(q_prime, 2)

print(q_prime)
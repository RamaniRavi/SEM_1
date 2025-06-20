# def build_term_doc_matrix(d1, d2, d3):
#     combined_docs = d1 + d2 + d3
#     vocab = set(combined_docs)

#     documents = [d1, d2, d3]

#     term_doc_matrix = []
#     for word in vocab:
#         presence = []
#         for document in documents:
#             presence.append(1 if word in document else 0)
#         term_doc_matrix.append((word, presence))

#     for term, vector in term_doc_matrix:
#         print(f"{term}: {vector}")

# d1 = ["python", "anaconda", "jupyter", "programming", "learn", "computer"]
# d2 = ["game", "are", "world", "programming", "learn", "learn", "are"]
# d3 = ["learn", "are", "world", "programming"]

# build_term_doc_matrix(d1, d2, d3)

def my_TD_matrix(d1, d2, d3):
    combined_docs = d1 + d2 + d3
    vocab = set(combined_docs)

    documents = [d1, d2, d3]
    doc_names = ["d1", "d2", "d3"]

    term_doc_dict = {}

    for word in vocab:
        presence = []
        for document in documents:
            presence.append(1 if word in document else 0)
        term_doc_dict[word] = presence

    return term_doc_dict, doc_names


def boolean_retrieval(term1, term2, d1, d2, d3):
    td_dict, doc_names = my_TD_matrix(d1, d2, d3)

    if term1 not in td_dict or term2 not in td_dict:
        print("One or both terms not found in the document collection.")
        return []

    result_vector = [
        t1 & t2 for t1, t2 in zip(td_dict[term1], td_dict[term2])
    ]
    result_docs = [
        doc_names[i] for i, val in enumerate(result_vector) if val == 1
    ]

    return result_docs


d1 = ["python", "anaconda", "jupyter", "programming", "learn", "computer"]
d2 = ["game", "are", "world", "programming", "learn", "learn", "are"]
d3 = ["learn", "are", "world", "programming"]

results = boolean_retrieval("python", "learn", d1, d2, d3)
print("Documents containing 'python AND learn':", results)

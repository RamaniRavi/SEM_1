import pandas as pd
import numpy as np
from sklearn.preprocessing import normalize
from sklearn.metrics.pairwise import cosine_similarity
from IPython.display import display

tfidf_df = pd.DataFrame([
    [0.3, 0.0, 0.2, 0.0], # d1 (relevant)
    [0.1, 0.4, 0.3, 0.0], # d2 (non-relevant)
    [0.0, 0.1, 0.2, 0.5], # d3
    [0.4, 0.4, 0.0, 0.0], # d4 (relevant)
    [0.0, 0.0, 0.4, 0.6]  # d5 (non-relevant)
], index=["d1", "d2", "d3", "d4", "d5"], columns=["term1", "term2", "term3", "term4"])

query_vector = pd.Series([0.6, 0.6, 0.3, 0.0], index=tfidf_df.columns)
query_vector = pd.Series(normalize(query_vector.values.reshape(1, -1))[0], index=tfidf_df.columns)

relevance_feedback = {
    'relevant': {'d1': 1.0, 'd4': 0.8},
    'non_relevant': {'d2': 1.0, 'd5': 0.6}
}

def rocchio_weighted(query_vector, tfidf_df, feedback_dict, alpha=1.0, beta=1.0, gamma=4.0, normalize_output=True):
    relevant_docs = list(feedback_dict['relevant'].keys())
    non_relevant_docs = list(feedback_dict['non_relevant'].keys())
    rel_weights = np.array([feedback_dict['relevant'][d] for d in relevant_docs])
    nonrel_weights = np.array([feedback_dict['non_relevant'][d] for d in non_relevant_docs])
    rel_matrix = tfidf_df.loc[relevant_docs].to_numpy()
    nonrel_matrix = tfidf_df.loc[non_relevant_docs].to_numpy()

    rel_centroid = np.average(rel_matrix, axis=0, weights=rel_weights)
    nonrel_centroid = np.average(nonrel_matrix, axis=0, weights=nonrel_weights)

    updated_query = alpha * query_vector.to_numpy() + beta * rel_centroid - gamma * nonrel_centroid

    if normalize_output:
        updated_query = normalize(updated_query.reshape(1, -1))[0]

    return pd.Series(updated_query, index=query_vector.index)

updated_query_vector = rocchio_weighted(query_vector, tfidf_df, relevance_feedback)

cos_sim_before = cosine_similarity(tfidf_df.values, query_vector.values.reshape(1, -1))
cos_sim_after = cosine_similarity(tfidf_df.values, updated_query_vector.values.reshape(1, -1))

ranked_docs_before = pd.Series(cos_sim_before.flatten(), index=tfidf_df.index).sort_values(ascending=False)
ranked_docs_after = pd.Series(cos_sim_after.flatten(), index=tfidf_df.index).sort_values(ascending=False)
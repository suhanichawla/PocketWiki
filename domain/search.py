from sentence_transformers import util
import numpy as np

# Function to search for the most relevant articles by title
def search_articles(query, encoded_titles, articles_dict, model, top_k=5):
    query_embedding = model.encode(query, convert_to_tensor=True)
    cos_scores = util.pytorch_cos_sim(query_embedding, encoded_titles)[0]
    cos_scores = cos_scores.cpu()

    top_results = np.argpartition(-cos_scores, range(top_k))[0:top_k]

    result_titles = []
    for idx in top_results:
        title = list(articles_dict.keys())[idx]
        result_titles.append((title, articles_dict[title], cos_scores[idx]))
    return result_titles

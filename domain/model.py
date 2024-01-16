from sentence_transformers import SentenceTransformer
MODEL_NAME = 'all-MiniLM-L6-v2'

# Function to initialize the model
def load_model():
    return SentenceTransformer(MODEL_NAME)

# Function to encode article titles into embeddings
def encode_articles(model, articles_dict):
    titles = list(articles_dict.keys())
    return model.encode(titles, convert_to_tensor=True)

# Function to encode article titles into embeddings
def encode_article_data(model, articles_dict):
    articles = list(articles_dict.values())
    return model.encode(articles, convert_to_tensor=True)

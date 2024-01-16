from sentence_transformers import SentenceTransformer

# Function to initialize the model
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

# Function to encode article titles into embeddings
def encode_articles(model, articles_dict):
    titles = list(articles_dict.keys())
    return model.encode(titles, convert_to_tensor=True)

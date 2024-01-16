import streamlit as st
from domain.model import load_model, encode_articles
from domain.search import search_articles
from components.search_bar import display_search_bar
from components.article_display import display_article_results
from domain.data_fetch import download_articles

def main():
    st.title("Article Search App")

    if 'articles' not in st.session_state:
        print("article collection started")
        st.session_state.articles = download_articles(10)
    
    articles_dict = st.session_state.articles
    model = load_model()
    encoded_titles = encode_articles(model, articles_dict)

    if st.button("Refresh Articles"):
        articles_dict = download_articles(5)  # Refresh the articles
        encoded_titles = encode_articles(model, articles_dict)

    query = display_search_bar()

    if query:
        results = search_articles(query, encoded_titles, articles_dict, model)
        display_article_results(results)

if __name__ == "__main__":
    main()

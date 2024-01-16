import streamlit as st
from domain.model import load_model, encode_articles
from domain.search import search_articles
from components.search_bar import display_search_bar
from components.article_display import display_article_results
from domain.data_fetch import download_articles

def get_save_articles(refresh=False):
    if 'articles' not in st.session_state or 'article_links' not in st.session_state or refresh==True:
        print("article collection started")
        st.session_state.articles, st.session_state.article_links = download_articles(5)
    return st.session_state.articles, st.session_state.article_links

def main():
    st.title("Article Search App")
    
    articles_dict, article_links = get_save_articles()
    model = load_model()
    encoded_titles = encode_articles(model, articles_dict)

    if st.button("Refresh Articles"):
        articles_dict, article_links = get_save_articles(refresh=True)
        encoded_titles = encode_articles(model, articles_dict)

    query = display_search_bar()

    if query:
        results = search_articles(query, encoded_titles, articles_dict, model)
        display_article_results(results, article_links)

if __name__ == "__main__":
    main()

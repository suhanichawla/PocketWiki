import streamlit as st

def display_article_results(results):
    for title, (content), score in results:
        st.subheader(title)
        st.write(content[:200] + "...")
        st.write(f"[Read More]({'https://google.com'})")
        st.text(f"Relevance Score: {score:.4f}")

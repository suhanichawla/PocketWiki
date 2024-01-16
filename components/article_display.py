import streamlit as st

def display_article_results(results, links):
    for title, (content), score in results:
        st.subheader(title)
        st.write(content[:200] + "...")
        st.write(f"[Read More]({links[title]})")
        st.text(f"Relevance Score: {score:.4f}")

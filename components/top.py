import streamlit as st
from .translations import translations 

def top(language):
    texts = translations[language]
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("# ADVANCING  \n # A BETTER WORLD  \n # WITH TECHNOLOGY")
        st.markdown("<br>", unsafe_allow_html=True)
        st.write(texts["top1"])
    with col2:
        st.image('/img/topRight.png', width=400)
    st.markdown('---')
    
    
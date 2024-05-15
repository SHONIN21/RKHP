import streamlit as st
from .translations import translations 

def portfolio(language):
    texts = translations[language]
    st.subheader("PORTFOLIO")
    st.write(texts["portfolio0"])
    tabs = st.tabs([texts["portfolio1"][0],texts["portfolio1"][1],texts["portfolio1"][2]])
    with tabs[0]:
        st.write(texts["portfolio2"][0])
        st.image("./img/po0.png",use_column_width=True)
    with tabs[1]:
        st.write(texts["portfolio2"][1])
        st.image("./img/po1.png",use_column_width=True)
    with tabs[2]:
        st.write(texts["portfolio2"][2])
        st.image("./img/po2.png",use_column_width=True)
    
    st.markdown('---')
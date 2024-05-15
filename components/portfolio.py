import streamlit as st
from .translations import translations 

def portfolio(language):
    texts = translations[language]
    st.subheader("PORTFOLIO")
    st.write(texts["portfolio0"])
    tabs = st.tabs([texts["portfolio1"][0],texts["portfolio1"][1],texts["portfolio1"][2]])
    with tabs[0]:
        st.write(texts["portfolio2"][0])
        st.image("../HP/img/po0.png",width=800)
    with tabs[1]:
        st.write(texts["portfolio2"][1])
        st.image("../HP/img/po1.png",width=800)
    with tabs[2]:
        st.write(texts["portfolio2"][2])
        st.image("../HP/img/po2.png",width=800)
    
    st.markdown('---')
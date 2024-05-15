import streamlit as st
from .translations import translations 

def team(language):
    st.subheader("TEAM")
    texts = translations[language]
    col1, col2 = st.columns(2)
    with col1:
        url0 = "https://www.linkedin.com/in/seiyo-ryo-46ba48201/"
        st.image("../HP/img/ryo.png",width=240)
        st.subheader("Seiyo Ryo")
        st.write(texts["team1"][0])
        st.link_button("Linkedin",url0,type="secondary")
    with col2:
        url1 = "https://www.linkedin.com/in/kensei-tanaka-25b572305/"
        st.image("../HP/img/kensei.png",width=240)
        st.subheader("Kensei Tanaka")
        st.write(texts["team1"][1])
        st.link_button("Linkedin",url0,type="secondary")
    st.markdown('---')
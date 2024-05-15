import streamlit as st
from .translations import translations 

def service(language):
    texts = translations[language]
    st.subheader("SERVICE")
    st.write(texts["service0"])
    col1, col2, col3 = st.columns(3)
    with col1:
        url0 = "https://www.lancers.jp/profile/wakaba01?ref=header_menu"
        st.image("../HP/img/serviceData.png",width=240)
        st.subheader(texts["service1"][0])
        st.write(texts["service2"][0])
        st.link_button(texts["button"],url0,type="secondary")
    with col2:
        url1 = "https://www.lancers.jp/profile/wakaba01?ref=header_menu"
        st.image("../HP/img/serviceConsulting.png",width=240)
        st.subheader(texts["service1"][1])
        st.write(texts["service2"][1])
        st.link_button(texts["button"],url1,type="secondary")
    with col3:
        url2 = "https://www.lancers.jp/profile/wakaba01?ref=header_menu"
        st.image("../HP/img/serviceAI.png",width=240)
        st.subheader(texts["service1"][2])
        st.write(texts["service2"][2])
        st.link_button(texts["button"],url2,type="secondary")
    st.markdown('---')
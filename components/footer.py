import streamlit as st
from .translations import translations 

def footer(language):
    texts = translations[language]
    st.subheader('CONTACT')
    with st.form("contact_form"):
        st.write(texts["contact"][0])
        name = st.text_input(texts["contact"][1]+"*")
        email = st.text_input(texts["contact"][2]+"*")
        about = st.text_input(texts["contact"][3]+"*")
        message = st.text_area(texts["contact"][4]+"*")
        submitted = st.form_submit_button(texts["contact"][5])
        if submitted:
            if name and email and about and message:
                st.success("送信が完了しました。")
            else:
                st.error("すべてのフィールドを入力してください。")
    st.markdown('---')
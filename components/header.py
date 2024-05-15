import streamlit as st

def header():
    col1, col2 = st.columns(2)
    with col2:
        language = st.radio(label="言語 / Language",
                            options=("日本語","English"),
                            index=0,
                            horizontal=True)
    with col1:
        st.subheader("RK Technology")
    st.markdown('---')
    return language

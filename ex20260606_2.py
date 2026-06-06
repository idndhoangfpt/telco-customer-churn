import streamlit as st

st.title("Hello Streamlit")

name = st.text_input("Nhập tên")

if name:
    st.write(f"Xin chào {name}")
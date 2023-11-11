import streamlit as st

#Title
st.title('Streamlit Tutorial')

#Header/Subheader
st.header('This is header')
st.subheader('This is subheader')

#Text
st.text("Hello Streamlit!!")

#파일 업로드
file = st.file_uploader("Upload your Menu Image", type=['jpg','png','jpeg'] )

st.image(file)q
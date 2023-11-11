import streamlit as st
from llm import *
from ocr import *
from preprocess import *

#Title
st.title('Streamlit Tutorial')

#Header/Subheader
st.header('This is header')
st.subheader('This is subheader')

#Text
st.text("Hello Streamlit!!")

#파일 업로드
file = st.file_uploader("Upload your Menu Image", type=['jpg','png','jpeg'] )

#OCR 실행
#text = ocr.extract()

#llm 실행
#result = llm.extract()

#Format 변환
#output = 
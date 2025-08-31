import streamlit as st
import helper
import pickle
import nltk

model = pickle.load(open('XGB_BOW_Model.pkl', 'rb'))

st.header("Duplicate Question Pairs")
st.subheader("Enter two questions to check if they are duplicates")

question1 = st.text_input("Enter Question 1")

question2 = st.text_input("Enter Question 2")

if st.button("find"):
    query = helper.query_point_creator(question1, question2)
    result = model.predict(query)[0]

    if result:
        st.header("Duplicate Questions")
    else:
        st.header("Non Duplicates Questions")
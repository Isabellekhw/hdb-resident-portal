import streamlit as st

st.title("HDB Resident AI Portal")

st.write("Welcome to the AI-powered resident issue system")

user_input = st.text_area("Describe your issue:")

if st.button("Submit"):
    st.write("Processing your request...")

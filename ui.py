import streamlit as st

st.title("LOGIN PAGE")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=0, max_value=120)
email = st.text_input("Enter your email")

gender = st.radio(
    "Enter your gender",
    ["Male", "Female"]
)

dob = st.date_input("Enter your date of birth")

if st.button("Submit"):
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Email:", email)
    st.write("Gender:", gender)
    st.write("Date of Birth:", dob)

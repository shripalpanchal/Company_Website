import streamlit as st
from send_email import send_email

st.header("Contact Us")

with st.form(key="Email Forms"):
    user_email = st.text_input("Enter Your Email:-")
    user_message =st.text_area("Enter Message her")
    message = f"""\
Subject : New email from {user_email}
From: {user_email}
{user_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        print(message)
        send_email(message)
import streamlit as st
import google.generativeai as genai

st.title("My Ai")

genai.configure(api_key="AIzaSyBRaTRzVGuKD6JDeS6Bc6-2h10cgdqsVtc")

text = st.text_input("Enter your question") 

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

if st.button("Click me"):
    response = chat.send_message(text)
    st.write(response.text)
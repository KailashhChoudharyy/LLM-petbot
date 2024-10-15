from dotenv import load_dotenv
load_dotenv()

import streamlit as st 
import os 
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text


st.set_page_config(page_title="Google gemini chatbot", page_icon="🐾")
st.title("Personal GPT for instant assistance of your pet")
# st.sidebar.success("How can I help you")
input=st.text_input("Input: " , key="input")
submit = st.button("Get Response")


if submit:
    response = get_gemini_response(input)
    st.subheader("Response to your question is ")
    st.write(response)
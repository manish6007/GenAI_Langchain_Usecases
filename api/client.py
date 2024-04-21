import streamlit as st
import requests
import os

from dotenv import load_dotenv
load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
def get_openai_response(input_text):
    response = requests.post(
        "http://localhost:8000/synonym/invoke",
        json={'input': {'topic':input_text}}
    )
    return response.json()['output']['content']

def get_ollama_response(input_text):
    response = requests.post(
        "http://localhost:8000/antonym/invoke",
        json={'input': {'topic':input_text}}
    )
    return response.json()['output']

## streamlit framework

st.title('Langchain with openai LLAMA3 API chains')
input_text = st.text_input('Write the synonym of')
input_text1 = st.text_input('Write the antonym of')
if input_text:
    st.write(get_openai_response(input_text))

if input_text1:
    st.write(get_ollama_response(input_text1))
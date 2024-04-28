from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

# Prompt Template
prompt=ChatPromptTemplate.from_messages([
        ("system","You are a AWS Solution Architect. Please provide solution of user queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework

st.title('Langchain App With OPENAI API')
input_text=st.text_input("Type the topic you want to explore")

#openai LLm
llm=ChatOpenAI(model_name="gpt-4")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))

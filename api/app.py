from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate # type: ignore
from langchain.chat_models import ChatOpenAI # type: ignore
from langserve import add_routes # type: ignore
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A Simple API Server"
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
    )

## OpenAI llm model
model=ChatOpenAI()

## ollama llm model
llm = Ollama(model="llama3")

prompt1=ChatPromptTemplate.from_template("Write a synonym of {topic}")
prompt2=ChatPromptTemplate.from_template("Write a antonym of {topic}")

add_routes(
    app,
    prompt1|model,
    path="/synonym"
)

add_routes(
    app,
    prompt2|llm,
    path="/antonym"
)

if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=8000)
# from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")

prompt =ChatPromptTemplate.from_messages([
    ("system", "You are an AI assistant. You will be given a task. You must generate a detailed and long answer."),
    ("user", "Please answer the following question: {question}"),
    # ("assistant", "{response}")
])

##Streamlit framework

st.title('Langchain Demo with LLama')
input_text = st.text_input("Search the topic needed")

from langchain_ollama import ChatOllama
llm = ChatOllama(model="llama3")
# llm = Ollama(model="llama3")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question" : input_text}))

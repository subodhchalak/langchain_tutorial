# Doc: https://python.langchain.com/docs/integrations/chat/openai/


import os
from langchain_ollama import ChatOllama
import streamlit as st
from langchain.globals import set_debug

set_debug(True)





OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


llm = ChatOllama(
    model="mistral:latest",
    temperature=0,
    # other params...
)


st.title("This is the streamlit demo for Langchain")
question = st.text_input("Please enter your question")

if question:
    response = llm.invoke(question)
    st.write(response.content)
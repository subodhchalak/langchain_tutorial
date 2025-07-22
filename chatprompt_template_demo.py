from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain.globals import set_debug
import streamlit as st

set_debug(True)


llm = ChatOllama(
    model="mistral:latest",
    temperature=0,
    # other params...
)


prompt_template = ChatPromptTemplate(
    [
        ("system", "You are a Agile coach. Answer the question related to Agile methodology."),
        ("human", "{question}")
    ]
)

st.title("Agile Coach")
question = st.text_input("Please enter your question")

if question:
    response = llm.invoke(prompt_template.format(question=question))
    st.write(response.content)
else:
    st.warning("Please enter your question")
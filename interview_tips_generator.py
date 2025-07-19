from langchain_ollama import ChatOllama
from langchain.globals import set_debug
from langchain_core.prompts import PromptTemplate
import streamlit as st

set_debug(True)


llm = ChatOllama(
    model = "mistral:latest",
    temperature = 0
)


prompt = PromptTemplate(
    input_variables = ["company", "position"],
    template = """
    You are a career guide expert. User is wants to join a {company} company and the {position}.
    Provide a details tips on the skills required to get this job and give some interview tips.
    """
)


st.title("Interview Tips Generator")

company = st.text_input("Please enter the company name")
position = st.text_input("Please enter the position")

if company and position:
    response = llm.invoke(
        prompt.format(
            company=company,
            position=position
        )
    )
    st.write(response.content)
else:
    st.write("Please enter the company and position name")

from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
import streamlit as st
from langchain.globals import set_debug

set_debug(True)



llm = ChatOllama(
    model="mistral:latest",
    temperature=0,
    # other params...
)

prompt = PromptTemplate(
    input_variables=["state", "paras", "language"],
    template="""
        You are the expert of the tranditonal cuisines of the Indian states.
        Avoid giving information about the fictional state or places.
        If the give state is fictionalor non-existant answer: I don't know.
        Question: Tell me a famous traditional cuisines of state of {state} from India.
        Answer in {paras} paras in {language}.
    """
)


st.title("Famous Meal Dishes from India")

state = st.text_input("Please enter the name of the state:")
paras = st.number_input("Please enter the number of paras:", min_value=1, max_value=3)
language = st.text_input("Please enter the language:")

if state:
    response = llm.invoke(prompt.format(state=state, paras=paras, language=language))
    st.write(response.content)
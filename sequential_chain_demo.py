from langchain_ollama import ChatOllama
from langchain.globals import set_debug
from langchain_core.prompts import PromptTemplate
import streamlit as st

set_debug(True)


llm = ChatOllama(
    model = "mistral:latest",
    temperature = 0
)


title_prompt = PromptTemplate(
    input_variables = ["topic"],
    template = """
    You are an experienced speech writer.
    You need to craft an impactful title for a speech
    on the following topic: {topic}
    Answer exactly with one title.
    """
)

speech_prompt = PromptTemplate(
    input_variables = ["title"],
    template = """
    You need to write a powerful speech of 350 words
    for the following title: {title}
    """
)


st.title("Speech Writing Assistant")
topic = st.text_input("Please enter the topic of the speech")

if topic:
    title_chain = title_prompt | llm
    title_chain_response = title_chain.invoke(
        {
            "topic": topic
        }
    )

    speech_chain = speech_prompt | llm
    speech_chain_response = speech_chain.invoke(
        {
            "title": title_chain_response
        }
    )

    st.subheader("Speech Title")
    st.write(title_chain_response.content)
    st.subheader("Speech")
    st.write(speech_chain_response.content)
    
else:
    st.write("Please enter the topic of the speech")




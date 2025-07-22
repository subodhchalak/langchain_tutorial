from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain.globals import set_debug
import streamlit as st
import json
set_debug(True)


llm = ChatOllama(model="mistral")


speech_title_template = PromptTemplate(
    input_variables = ["topic"],
    template = """
    You are an experienced speech writer.
    You need to craft an impactful title for a speech
    on the following topic: {topic}
    Answer exactly with one title.
    """
)

speech_template = PromptTemplate(
    input_variables = ["topic", "emotion"],
    template = """
    You need to write a powerful speech of 350 words
    for the following title: {title} and emotion: {emotion}
    """
)

st.title("Speech Title Generator")
topic = st.text_input("Enter the topic for the speech")
emotion = st.text_input("Enter the emotion for the speech")


if topic and emotion:
    speech_title_chain = speech_title_template | llm
    speech_title_response = speech_title_chain.invoke({"topic": topic})
    speech_title = speech_title_response.content

    speech_chain = speech_template | llm
    speech_response = speech_chain.invoke({"title": speech_title, "emotion": emotion})
    speech_text = speech_response.content

    # st.header("Speech Title")
    # st.write(speech_title)

    # st.header("Speech")
    # st.write(speech_text)
    st.json(
        {
            "title": speech_title,
            "speech": speech_text
        },
        expanded=False
    )

else:
    st.warning("Please enter a topic and emotion.")


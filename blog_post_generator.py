from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain.globals import set_debug
from langchain_core.output_parsers.string import StrOutputParser
import streamlit as st

set_debug(True)


llm = ChatOllama(
    model = "mistral:latest",
    temperature = 0,
    # other params...
)

blog_outline_prompt = PromptTemplate(
    input_variables = ["topic"],
    template = """
        You are a professional blogger.
        Create an outline for a blog post on the following topic: {topic}
        The outline should include:
        - Introduction
        - 3 main points with subpoints
        - Conclusion
    """
)

blog_content_prompt = PromptTemplate(
    input_variables = ["outline"],
    template = """
        You are a professional blogger.
        Write an engaging introduction paragraph based on the following
        outline:{outline}
        The introduction should hook the reader and provide a brief
        overview of the topic.
    """
)

st.title("Blog Outline Generator")
topic = st.text_input("Please enter the blogpost topic")


if topic:
    blog_outline_chain = blog_outline_prompt | llm | StrOutputParser() | (lambda outline: (st.write(outline), outline))
    blog_content_chain = blog_content_prompt | llm

    final_chain = blog_outline_chain | blog_content_chain


    final_chain_response = final_chain.invoke(
        {
            "topic": topic
        }
    )
    st.write(final_chain_response.content)
else:
    st.write("Please enter a topic")

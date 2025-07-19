from langchain_ollama import ChatOllama
from langchain.globals import set_debug
from langchain_core.prompts import PromptTemplate
import streamlit as st


set_debug(True)


llm = ChatOllama(
    model="mistral:latest",
    temperature=0,
    # other params...
)


prompt = PromptTemplate(
    input_variables=["city", "month", "language", "budget"],
    template = """
    Welcome to the {city} travel guide!
    If you're visiting in {month}, here's what you can do:
        1. Must-visit attractions.
        2. Local cuisine you must try.
        3. Useful phrases in {language}.
        4. Tips for traveling on a {budget} budget in Indian Rupees.
        Enjoy your trip!
    """
)

st.title("City Travel Guide")

city = st.text_input("Enter the name of the city")
month = st.text_input("Enter the name of the month")
language = st.text_input("Enter the language")
budget = st.selectbox("Select the budget", ["low", "medium", "high"])
# budget = st.number_input("Please enter the budget in numerical value")


if city and month and language and budget:
    response = llm.invoke(
        prompt.format(
            city=city,
            month=month,
            language=language,
            budget=budget
        )
    )
    st.write(response.content)
else:
    st.write("Please enter the city, month, language and budget")
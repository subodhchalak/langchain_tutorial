# Doc: https://python.langchain.com/docs/integrations/chat/openai/


import os
import asyncio
# from langchain_community.chat_models import ChatOllama
from langchain_ollama import ChatOllama


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


llm = ChatOllama(
    model="mistral:latest",
    temperature=0,
    # other params...
)



async def call_llm():
    question = input("please enter your question: ")
    await llm.ainvoke(question)
    # print(response)


asyncio.run(call_llm())
# print(response)
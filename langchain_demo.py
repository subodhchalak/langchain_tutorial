# Doc: https://python.langchain.com/docs/integrations/chat/openai/


import os
from langchain_openai import ChatOpenAI


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# instantiate the LLM
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=OPENAI_API_KEY,  # if you prefer to pass api key in directly instaed of using env vars
    # base_url="...",
    # organization="...",
    # other params...
)



question = input("please enter your question: ")
response = llm.invoke(question)
print(response)
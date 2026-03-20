# 6. Use gpt-4o-mini to generate Python code for a simple calculator.

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    temperature=0.2
)

prompt = PromptTemplate.from_template(
    template="""Generate complete Python code for a simple calculator"""
)

response = llm.invoke(prompt.format())
print(response.content)

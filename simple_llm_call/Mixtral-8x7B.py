# 8.	Use Mixtral 8x7B to generate a basic HTML webpage for a personal portfolio.

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    model="mistralai/mixtral-8x7b-instruct",  
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    temperature=0.7,
    max_tokens=1000
)

prompt = PromptTemplate.from_template(
    template="""Generate a complete HTML webpage for a personal portfolio"""
)
response = llm.invoke(prompt.format())
print(response.content)

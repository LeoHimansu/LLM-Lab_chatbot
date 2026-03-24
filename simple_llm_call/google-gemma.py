
# 9.	Use google/gemma to create a math quiz with 5 questions.

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os 

load_dotenv()

llm = ChatOpenAI(
    model="google/gemma-3-27b-it:free",  
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

prompt = PromptTemplate.from_template(
    template="Create a math quiz with 5 questions."
)

response = llm.invoke(prompt.format())
print(response.content)

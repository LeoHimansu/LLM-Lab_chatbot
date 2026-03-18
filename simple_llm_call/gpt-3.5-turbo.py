
# 2.	Use Gemini 1.5 Pro to summarize a given paragraph in 3–4 sentences.

import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    temperature=0.7
)


paragraph = """Artificial Intelligence has transformed numerous industries in recent years. 
From healthcare to finance, AI systems are being deployed to automate tasks, 
analyze vast amounts of data, and make predictions with unprecedented accuracy. 
Machine learning algorithms can now detect diseases from medical images better 
than human experts in some cases. However, this rapid advancement also raises 
important ethical questions about privacy, job displacement, and the need for 
proper regulation. As AI continues to evolve, society must adapt to harness its 
benefits while mitigating potential risks."""

prompt = PromptTemplate.from_template(
    template="Summarize the following paragraph in 3-4 sentences:\n\n{text}"
)

chain = prompt | llm

response = chain.invoke({"text": paragraph})
print(response.content)
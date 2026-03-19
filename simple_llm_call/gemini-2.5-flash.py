# 2.	Use gemini-2.5-flash to summarize a given paragraph in 3–4 sentences.

import os
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()



llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite",max_tokens=200)


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

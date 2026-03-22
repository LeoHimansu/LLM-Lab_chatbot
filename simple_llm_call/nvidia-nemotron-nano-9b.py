# 7.	Use nvidia/nemotron-nano-9b to explain Blockchain technology in simple terms.

from langchain_nvidia_ai_endpoints import ChatNVIDIA
from dotenv import load_dotenv
import os

load_dotenv()

llm= ChatNVIDIA(model="nvidia/nemotron-nano-9b-v2:free",
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY"))

print(llm.invoke("explain blockchain technology in 1 line  ").content)

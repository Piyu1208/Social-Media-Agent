from dotenv import load_dotenv
import os
from openai import OpenAI
from agents.context_agent import ContextAgent


load_dotenv()

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("API_KEY")
    )

model = "llama-3.3-70b-versatile"

agent = ContextAgent(client, model)

context = agent.run(".")

print(context)
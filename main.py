from openai import OpenAI
from agents.context_agent import ContextAgent


client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=""
    )

model = "llama-3.3-70b-versatile"

agent = ContextAgent(client, model)

context = agent.run(".")

print(context)
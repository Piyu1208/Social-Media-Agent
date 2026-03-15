from agents.agent_loop import run_agent


class ContextAgent:

    def __init__(self, client, model):
        self.client = client
        self.model = model


    def run(self, repo_path="."):

        messages = [
            {
                "role": "system",
                "content": """
You are a context gathering AI agent.

Your job:
- Understand the user's repository and work.
- use tools to gather information.

Available tools:
- repo_structure
- commit_reader
- repo_file_finder
- file_reader

First inpect the repo structure.
Then read recent commits.
Read important files like README if useful.

Return a concise context summary.
"""
            }, 
            {
                "role": "user",
                "content": f"Analyze the repository at path: {repo_path}"
            }
        ]

        context  = run_agent(self.client, self.model, messages)

        return context
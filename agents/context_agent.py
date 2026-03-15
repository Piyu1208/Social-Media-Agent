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

                            Your job is to thoroughly analyze a repository by following these steps IN ORDER:

                            1. Call repo_structure to see all files.
                            2. Call commit_reader to read ALL recent commits (use limit=20).
                            3. Call file_reader on EVERY .py file you see in the structure - agents/, tools/, and root level files.
                            4. If a README exists, read it. If not, skip and continue.

                            Do NOT stop after failing to find README.
                            Do NOT summarize until you have read the actual .py source files.
                            You MUST call file_reader on at least: main.py, and all files inside agents/ and tools/.

                            After reading all files, return a detailed summary covering:
                            - What the project does
                            - How the agents and tools work
                            - The flow from main.py through the agent loop
                            """
            },
            {
                "role": "user",
                "content": f"Analyze the repository at path: {repo_path}"
            }
    ]

        context  = run_agent(self.client, self.model, messages)

        return context
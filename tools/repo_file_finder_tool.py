import os
from .base_tool import BaseTool

class RepoFileFinderTool(BaseTool):
    name = "repo_file_finder"
    description = "Finds files in a repository matching a keyword."

    IGNORED_DIRS = {".git", "__pycache__", "node_modules", "venv", ".venv"}

    def run(self, repo_path=".", keyword=None, limit=20):
        matches = []

        for root, dirs, files in os.walk(repo_path):

            dirs[:] = [d for d in dirs if d not in self.IGNORED_DIRS]

            for file in files:

                if keyword and keyword.lower() not in file.lower():
                    continue

                matches.append(os.path.join(root, file))

                if len(matches) >= limit:
                    return "\n".join(matches)
                
        return "\n".join(matches)
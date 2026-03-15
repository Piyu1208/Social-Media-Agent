import os
from .base_tool import BaseTool

class RepoStructureTool(BaseTool):
    name = "repo_structure"
    description = "Returns a tree like strucutre of the repository"

    IGNORED_DIRS = {".git", "__pycache__", "node_modules", "venv", ".venv"}


    def run(self, repo_path, max_depth=3):

        structure = []

        for root, dirs, files in os.walk(repo_path):

            dirs[:] = [d for d in dirs if d not in self.IGNORED_DIRS]

            depth = root.replace(repo_path, "").count(os.sep)

            if depth > max_depth:
                continue

            indent = "  " * depth

            folder = os.path.basename(root) or "./"

            structure.append(f"{indent}{folder}/")

            file_indent = indent + "  "

            for file in files:
                if file.startswith("."):
                    continue

                structure.append(f"{file_indent}{file}")

        return "\n".join(structure)



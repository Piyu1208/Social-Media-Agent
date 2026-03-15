import subprocess
from .base_tool import BaseTool

class CommitReaderTool(BaseTool):
    name = "commit reader"
    description = "Reads recent git commits from repository."


    def run(self, repo_path=".", limit=5):

        cmd = [
            "git",
            "-C",
            repo_path,
            "log",
            f"-n{limit}",
            "--pretty=format:%h | %an | %s"
        ]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )

        return result.stdout
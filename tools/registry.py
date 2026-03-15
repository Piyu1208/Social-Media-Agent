# To let python execute the tools

from tools.repo_structure import RepoStructureTool
from tools.commit_reader import CommitReaderTool




TOOL_REGISTRY = {
    "repo_structure": RepoStructureTool(),
    "commit_reader": CommitReaderTool(),
}
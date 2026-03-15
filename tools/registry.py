# To let python execute the tools

from tools.repo_structure import RepoStructureTool
from tools.commit_reader import CommitReaderTool
from tools.repo_file_finder_tool import RepoFileFinderTool



TOOL_REGISTRY = {
    "repo_structure": RepoStructureTool(),
    "commit_reader": CommitReaderTool(),
    "repo_file_finder": RepoFileFinderTool(),
    
}
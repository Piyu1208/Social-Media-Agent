# To let python execute the tools

from tools.repo_structure import RepoStructureTool
from tools.commit_reader import CommitReaderTool
from tools.repo_file_finder_tool import RepoFileFinderTool
from tools.file_reader_tool import FileReaderTool

TOOL_REGISTRY = {
    "repo_structure": RepoStructureTool(),
    "commit_reader": CommitReaderTool(),
    "repo_file_finder": RepoFileFinderTool(),
    "file_reader": FileReaderTool()
}
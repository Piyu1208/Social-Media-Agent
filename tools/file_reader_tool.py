from .base_tool import BaseTool

class FileReaderTool(BaseTool):
    name = "file_reader"
    description = "Reads the contents of a file from the repository."

    def run(self, file_path, max_chars=4000):

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        return content[:max_chars]
    
    
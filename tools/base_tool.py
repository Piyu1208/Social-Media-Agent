class BaseTool:
    name = "base_tool"
    description = "Base tool interface"

    def run(self, **kwargs):
        raise NotImplementedError("Tool must implement run()")
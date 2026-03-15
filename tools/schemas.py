# Tells the LLM what tools exists

repo_structure_schema = {
    "type": "function",
    "function": {
        "name": "repo_structure",
        "description": "Returns the directory structure of a repository.",
        "parameters": {
            "type": "object",
            "properties": {
                "repo_path": {"type": "string"},
                "max_depth": {"type": "integer"}
            },
            "required": ["repo_path"]
        }
    }
}


commit_reader_schema = {
    "type": "function",
    "function": {
        "name": "commit_reader",
        "description": "Returns the recent git commits from repository.",
        "parameters": {
            "type": "object",
            "properties": {
                "repo_path": {"type": "string"},
                "limit": {"type": "integer"}
            },
            "required": []
        }
    }
}


repo_file_finder_schema = {
    "type": "function",
    "function": {
        "name": "repo_file_finder",
        "description": "Finds files in the repository by keyword.",
        "parameters": {
            "type": "object",
            "properties": {
                "repo_path": {"type", "string"},
                "keyword": {"type", "string"},
                "limit": {"type", "integer"}
            }
        }
    }
}




TOOLS_SCHEMA = [
    repo_structure_schema,
    commit_reader_schema,
    repo_file_finder_schema,
    
]
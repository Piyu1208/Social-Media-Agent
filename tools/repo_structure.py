import os

def get_repo_structure(repo_path, max_depth=3):
    """
    Returns a tree-like structure of the repository.
    """

    IGNORED_DIRS = {".git", "__pycache__", "node_modules", ".venv", "venv"}

    tree = []

    for root, dirs, files in os.walk(repo_path):

        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]

        depth = root.replace(repo_path, "").count(os.sep)

        if depth > max_depth:
            continue

        indent = "  " * depth

        folder = os.path.basename(root) or "./"

        tree.append(f"{indent}{folder}/")

        file_indent = indent + "  "

        for file in files:
            if file.startswith("."):
                continue

            tree.append(f"{file_indent}{file}")

    return "\n".join(tree)  


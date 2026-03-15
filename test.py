from tools.repo_structure import get_repo_structure

repo_path = "."

structure = get_repo_structure(repo_path)

print(structure) 


"""
import os

for root, dirs, files in os.walk("."):
    print(root)
    print(dirs)
    print(files)
    print("\n")

    """
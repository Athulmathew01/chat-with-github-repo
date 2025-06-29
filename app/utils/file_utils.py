from pathlib import Path
from typing import List

ACCEPTED_EXTENTIONS = [".pdf",".md",".txt",".json",".ts",".html",".css"]

EXCLUDED_DIRS = [".git","node_modules","__pycache__"]

def collect_valid_files(repo_path: Path) -> List[Path]:
    valid_files = []

    for file_path in repo_path.rglob("*"):
        if file_path.is_file():
            if file_path.suffix.lower() in ACCEPTED_EXTENTIONS:
                if not any(part in EXCLUDED_DIRS for part in file_path.parts):
                    valid_files.append(file_path)
                    
    return valid_files
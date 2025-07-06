from pathlib import Path
from typing import List

# Directories we don't want to crawl into
EXCLUDED_DIRS = [".git", "node_modules", "__pycache__"]

# File extensions to explicitly skip (binaries/heavy)
EXCLUDED_EXTENSIONS = [
    ".png", ".jpg", ".jpeg", ".gif", ".mp4", ".mp3", ".exe", ".dll",
    ".zip", ".tar", ".gz", ".7z", ".woff", ".ttf", ".otf", ".ico", ".bin",
    ".apk", ".svg"  # Optional: skip large PDFs unless parsed explicitly
]

# Optional: max file size in MB
MAX_FILE_SIZE_MB = 10


def collect_valid_files(repo_path: Path) -> List[Path]:
    valid_files = []

    for file_path in repo_path.rglob("*"):
        if file_path.is_file():
            if any(part in EXCLUDED_DIRS for part in file_path.parts):
                continue

            if file_path.suffix.lower() in EXCLUDED_EXTENSIONS:
                continue

            if file_path.stat().st_size > MAX_FILE_SIZE_MB * 1024 * 1024:
                continue

            valid_files.append(file_path)

    return valid_files

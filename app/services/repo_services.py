import subprocess
from pathlib import Path
import uuid


def _generate_repo_path() -> Path:
    repo_id = str(uuid.uuid4())[:8]
    return Path("repo") / f"repo_{repo_id}"

def clone_repo_shallow(repo_url: str) -> Path:
    
    repo_dir = _generate_repo_path()
    try:
        subprocess.run(["git", "clone", "--depth", "1", repo_url, str(repo_dir)], check=True)
    except subprocess.CalledProcessError as e:
        raise Exception(f"Git shallow clone failed: {e}")
    return repo_dir

def clone_repo_full(repo_url: str) -> Path:
    repo_dir = _generate_repo_path()

    try:
        subprocess.run(["git", "clone", repo_url,str(repo_dir)],check=True)
    except subprocess.CalledProcessError as e:
        raise Exception(f"Git full clone failed: {e}")
    return repo_dir



from fastapi import APIRouter, HTTPException
from pydantic  import BaseModel, HttpUrl
from pathlib import  Path
from typing import Literal
from app.services.repo_services import clone_repo_full, clone_repo_shallow
from app.utils.file_utils import collect_valid_files
from app.services.document_loader import load_documents
from app.services.chunk_service import chunk_documents
from app.services.embedding_service import embed_documents

router = APIRouter()

class RepoRequest(BaseModel):
    repo_url: HttpUrl
    mode: Literal["shallow", "full"] = "shallow"


@router.post("/upload-repo")
async def upload_repo(payload: RepoRequest):
    try:
        if payload.mode == "full":
            repo_path: Path = clone_repo_full(str(payload.repo_url))
        else:
            repo_path: Path = clone_repo_shallow(str(payload.repo_url))
        
        valid_files = collect_valid_files(repo_path)
        docs = load_documents(valid_files)
        chunks = chunk_documents(docs)
        embed_documents(chunks)
        return {
            "status": "success",
            "mode": payload.mode,
            "repo_path": str(repo_path),
            "total_files": len(valid_files),
            "files":[str(f.relative_to(repo_path)) for f in valid_files],
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to clone repo: {str(e)}")

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.query_service import run_query

class QueryRequest(BaseModel):
    question: str


router = APIRouter()

@router.post("/query")
async def handle_user_query(payload: QueryRequest):
    try:
        question = payload.question
        response = run_query(question)
        return {"answer": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



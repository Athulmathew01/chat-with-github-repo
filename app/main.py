from fastapi import FastAPI
from app.api import repo, query_router

app = FastAPI(title="Chat with your Github repo")

# include router from repo file
app.include_router(repo.router)
app.include_router(query_router.router, prefix="/api")
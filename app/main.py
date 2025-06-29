from fastapi import FastAPI
from app.api import repo

app = FastAPI(title="Chat with your Github repo")

# include router from repo file
app.include_router(repo.router)

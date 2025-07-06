from typing import List
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from app.core.config import EMBEDDING_MODEL,CHROMA_DIR
import os


os.environ["CHROMA_TELEMETRY_ENABLED"] = "false"

def embed_documents(chunks: List[Document], persist_dir: str = CHROMA_DIR) -> Chroma:
    embedding_model = OllamaEmbeddings(model=EMBEDDING_MODEL)

    vectorstore = Chroma.from_documents(
        documents = chunks,
        embedding = embedding_model,
        persist_directory = persist_dir
    )
    vectorstore.persist()
    return vectorstore

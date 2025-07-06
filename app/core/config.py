from dotenv import load_dotenv
import os

load_dotenv()

EMBEDDING_MODEL = os.getenv("OLLAMA_EMBEDDING_MODEL", "nomic-embed-text")
CHAT_MODEL = os.getenv("OLLAMA_CHAT_MODEL", "phi3")
CHROMA_DIR = os.getenv("CHROMA_PERSIST_DIR", "vector_store")
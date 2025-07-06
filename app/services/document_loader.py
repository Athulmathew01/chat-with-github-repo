from pathlib import Path
from typing import List
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader, TextLoader

def load_documents(file_paths: List[Path]) ->  List[Document]:
    documents = []

    for file_path in file_paths:
        ext = file_path.suffix.lower()
        try:
            if ext == ".pdf":
                loader = PyPDFLoader(str(file_path))
                docs = loader.load()
                for doc in docs:
                    doc.metadata["source"] = str(file_path)
                documents.extend(docs)
            else:
                loader = TextLoader(str(file_path), encoding="utf-8",autodetect_encoding=True)
                docs = loader.load()
                for doc in  docs:
                    doc.metadata["source"] = str(file_path)
                documents.extend(docs)
        except Exception as e:
            print(f"Skipping {file_path}: {e}")
    return documents




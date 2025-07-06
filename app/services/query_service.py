from langchain_community.vectorstores import Chroma
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_ollama import OllamaEmbeddings
from app.core.config import EMBEDDING_MODEL, CHROMA_DIR, CHAT_MODEL
from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnablePassthrough
from langchain.prompts import PromptTemplate


def load_vectorstore() -> Chroma:
    embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)
    vector_store = Chroma(
        persist_directory=CHROMA_DIR,
        embedding_function=embeddings
    )   
    return vector_store

def create_retriever(vectorstore: Chroma) -> VectorStoreRetriever:
    retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 8}
    )

    return retriever    

def run_query(query: str) -> str:
    vectorstore = load_vectorstore()

    retriever = create_retriever(vectorstore)

    llm = ChatOllama(model=CHAT_MODEL)

    template = """
        You are an expert software assistant. Analyze the following code documentation and answer the user's question based on it.

        Context:
        {context}

        Question:
        {question}
    """

    prompt = PromptTemplate(input_variables=["context", "question"], template=template)

    chain =(
        retriever
        | (lambda docs:{
            "context":"\n\n".join([doc.page_content for doc in docs]),
            "question": query
        })
        | prompt
        | llm
    )

    response = chain.invoke(query)

    return str(getattr(response, "content", response))
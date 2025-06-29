```markdown
# 💬 Chat with Your GitHub Repo

A FastAPI-powered backend service that allows users to upload or link to a GitHub repository and chat with its content using a local LLM powered by LangChain and Ollama.

---

## 🚀 Features

- 🔗 Accept GitHub repository URLs or ZIP uploads
- 📂 Recursively extract relevant source files (`.py`, `.md`, `.txt`, `.json`, etc.)
- 🧠 Process and embed source code with LangChain
- 💬 Enable natural language Q&A over the repository
- 🐳 Docker & Docker Compose support for local LLMs via Ollama

---

## 🏗️ Tech Stack

- **FastAPI** – Python web framework for building APIs
- **LangChain** – Framework for LLM applications
- **Ollama** – Local inference for LLMs like Mistral, LLaMA2
- **FAISS / Chroma** – Vector search (planned)
- **Docker** – Containerization and orchestration

---

## 📂 Folder Structure

```text
chat-github-repo/
├── app/
│   ├── main.py              # FastAPI entry point
│   ├── api/                 # API route handlers
│   │   └── repo.py          # /upload-repo route
│   ├── services/            # Cloning and processing logic
│   │   └── repo_service.py
│   ├── utils/               # Helper functions (e.g., file filter)
│   │   └── file_utils.py
│   └── .env          # Environment & configuration loader
├── repos/                   # Temp cloned repositories
├── requirements.txt         # Python dependencies
├── .gitignore               # Ignore .env, __pycache__, repos, etc.
└── README.md
```

---

## 🛠️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/chat-github-repo.git
cd chat-github-repo
```

### 2. Set Up Virtual Environment and Install Dependencies

```bash
python -m venv venv
source venv/bin/activate       # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run FastAPI Development Server

```bash
uvicorn app.main:app --reload
```

Open your browser at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🔮 Planned Features

- [ ] File chunking based on token limits  
- [ ] Embed source code using FAISS or ChromaDB  
- [ ] Chat interface over vector store + LangChain memory  
- [ ] Docker Compose setup with Ollama service  
- [ ] Add session support and multi-user handling  
- [ ] Optional frontend with Streamlit or Next.js

---

## 📝 License

This project is licensed under the [MIT License](LICENSE). You are free to use and adapt it for personal or commercial projects.

---

## 🙋‍♂️ Author

**Athul** – Backend-end Developer 
```

from fastapi import FastAPI, Query
from rag_project.src.embeddings.embedder import get_embedder
from rag_project.src.ingestion.loader import load_and_split
from rag_project.src.vectorstore.faiss import create_vector_index
from rag_project.src.llm.groq_llm import get_llm
from rag_project.src.pipeline.rag_chain import build_rag_chain

app = FastAPI()

# Load once on startup
urls = ["https://lilianweng.github.io/posts/2023-06-23-agent/"]
docs = load_and_split(urls)
embedder = get_embedder()
vector_index = create_vector_index(docs, embedder)
llm = get_llm()
rag_chain = build_rag_chain(vector_index, llm)

@app.get("/ask")
def ask_question(query: str = Query(..., description="Your question")):
    response = rag_chain.invoke({"input": query})
    return {"answer": response["answer"]}
from fastapi import FastAPI
from pydantic import BaseModel
from rag import RAGService

app = FastAPI(title="RAG PoC Chatbot")

rag_service = RAGService()

class AddDocRequest(BaseModel):
    text: str

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def root():
    return {"message": "RAG PoC Chatbot이 실행중 입니다!"}

@app.post("/add")
def add_document(req: AddDocRequest):
    rag_service.add_document(req.text)
    return {"status": "added"}

@app.post("/query")
def query(req: QueryRequest):
    answer = rag_service.answer_query(req.query)
    return {"answer": answer}
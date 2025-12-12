from llm import LLMService
from embedding import EmbeddingService
from vector_store import InMemoryVectorStore

class RAGService:
    def __init__(self):
        print("RAG 서비스 초기화 중")
        self.llm_service = LLMService()
        self.vector_store_service = InMemoryVectorStore(dim=384)  # 임베딩 벡터 차원 설정
        self.embedding = EmbeddingService()

    def add_document(self, text: str):
        vector = self.embedding.embed(text)
        self.vector_store_service.add_document(text, vector)
    
    def answer_query(self, query: str) -> str:
        query_vector = self.embedding.embed(query)
        relevant_docs = self.vector_store_service.search(query_vector, k=3)

        context = "\n".join(relevant_docs)
        prompt = f"""
        너는 유능한 건강 관련 AI 어시스턴트야. 다음은 질문에 답하는데 도움이 되는 문서들이야. 이 문서들을 참고해서 질문에 한문장으로 답해줘.
        
        Context:
        {context}

        Question: {query}
        
        Answer:
        """

        answer = self.llm_service.generate(prompt)
        return answer
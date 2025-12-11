import faiss
import numpy as np

class InMemoryVectorStore:
    def __init__(self, dim: int):
        self.dim = dim
        self.index = faiss.IndexFlatL2(dim)
        self.documents = []  # 저장된 텍스트 문서 리스트

    def add_document(self, text: str, vector: np.ndarray):
        vector = np.array(vector).astype("float32").reshape(1, -1)
        self.index.add(vector) # 모든 벡터를 인덱스에 추가
        self.documents.append(text) # 해당 벡터에 매핑되는 원본 텍스트 저장

    def search(self, query_vector: np.ndarray, k: int = 3):
        query_vector = np.array(query_vector).astype("float32").reshape(1, -1) # 사용자 입력 문장 임베딩 벡터     
        distances, indices = self.index.search(query_vector, k)
        results = []

        for idx in indices[0]:
            if idx < len(self.documents):
                results.append(self.documents[idx])

        return results
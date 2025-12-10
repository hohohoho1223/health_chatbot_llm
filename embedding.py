from sentece_transformers import SentenceTransformer
from dotenv import load_dotenv
import os

load_dotenv() # .env 파일에서 환경 변수 로드

EMBEDDING_MODEL_NAME = os.getenv("EMBED_MODEL")

class EmbeddingService:
    def __init__(self):
        print("임베딩 모델 로딩중...")
        self.model = SentenceTransformer(EMBEDDING_MODEL_NAME)

    def embed(self, text: str):
        return self.model.encode(text) # 텍스트를 임베딩 벡터로 변환(encode)
    
# 헬스케어 LLM 챗봇 서비스

## PoC(Proof of Concept) 목록

- Python FastAPI 기반으로 자체 LLM 서버 구축이 가능성 확인
- Qwen 3B 모델을 CPU 환경에서 로딩 및 실행이 가능한지 확인
- 간단한 RAG 구성(인메모리 FAISS 기반)이 정상적으로 작동하는지 확인

## 기능구현 목록(PoC 범위)

### 1. LLM 자체 모델 로딩

- [x] HugginFace 모델 다운로드
- [x] CPU 기반 실행 테스트(app.py)
- [x] 간단한 프롬프트 및 응답 테스트

### 2. 임베딩 기능 구현

- [x] Sentence-Transformer 기반 임베딩 구현
- [x] FAISS 인메모리 VectorStore 구현

### 3. RAG 기능 구현

- [x] 검색 기반 응답 생성 구현

## 응답 결과

![Qwen 2.5 0.5B RAG 응답 결과](poc_qwen_2_5_0_5b_rag_response.png)

## 기술 스택(PoC 기준)

- Python 3.11+
- FastAPI
- HuggingFace Transformers
- Sentence-Transformers
- FAISS(CPU)
- Uvicorn

## 브랜치 전략

- `feature/poc-llm-rag` 브랜치로 작업

## 커밋 전략

- 참고 링크: [Stephen Parish Commit Message Guide](https://gist.github.com/stephenparish/9941e89d80e2bc58a153)


## PoC 이후 확장 방향

- vLLM 기반 Qwen 가속 및 GPU(L4) 환경에서 구현
- 벡터DB 연동
- LangChain / LangGraph 기반 RAG Pipeline 구축
- SpringBoot & FastAPI 연동
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from dotenv import load_dotenv
import os

load_dotenv() # .env 파일에서 환경 변수 로드

Meodel_NAME = os.getenv("MODEL_NAME")

class LLMService:
    def __init__(self):
        print("LLM 모델 로딩중...")
        self.tokenizer = AutoTokenizer.from_pretrained(Meodel_NAME)
        self.model = AutoModelForCausalLM.from_pretrained(
            Meodel_NAME,
            torch_dtype=torch.float32,
            device_map="cpu"
        )

    def generate(self, prompt: str, max_new_tokens: int = 256) -> str: #프롬프트를 받아 답변 생성
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=True,
            temperature=0.7
        ) 
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
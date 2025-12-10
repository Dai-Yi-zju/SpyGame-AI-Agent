# agents/model.py
"""Model class for LLM initialization"""
from langchain_openai import ChatOpenAI
from typing import Optional


class GameModel:
    
    def __init__(
        self,
        api_key: str = "your api key",
        base_url: str = "https://api.siliconflow.cn/v1",
        model: str = "Qwen/Qwen2.5-32B-Instruct",
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        timeout: Optional[float] = 60.0
    ):
        self.api_key = api_key
        self.base_url = base_url
        self.model_name = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.timeout = timeout
        
        self.llm = ChatOpenAI(
            api_key=api_key,
            base_url=base_url,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            timeout=timeout
        )
    
    def get_llm(self) -> ChatOpenAI:
        return self.llm
    
    def __repr__(self) -> str:
        return f"GameModel(model={self.model_name}, base_url={self.base_url})"


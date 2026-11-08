from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ollama_base_url: str = "http://localhost:11434"
    qdrant_url: str = "http://localhost:6333"
    llm_model: str = "qwen2.5:7b-instruct-q4_K_M"
    embedding_model: str = "BAAI/bge-small-en-v1.5"
    collection_name: str = "airgap_rag"
    chunk_size: int = 512
    chunk_overlap: int = 64
    top_k: int = 4

    class Config:
        env_file = ".env"


settings = Settings()

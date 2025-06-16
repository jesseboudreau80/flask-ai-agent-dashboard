import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Flask configuration
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-dev-key')

    # LLM Configuration
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4o')
    OPENAI_BASE_URL = os.getenv('OPENAI_BASE_URL', 'https://api.openai.com/v1')

    # Ollama (local LLM)
    OLLAMA_API_BASE = os.getenv('OLLAMA_API_BASE')  # e.g., http://localhost:11434/api
    OLLAMA_MODEL = os.getenv('OLLAMA_MODEL')

    # Vector/Memory Settings
    ENABLE_MEMORY = os.getenv('ENABLE_MEMORY', 'false').lower() == 'true'
    VECTOR_DB_PATH = os.getenv('VECTOR_DB_PATH', './vector_store')

    # File Uploads
    MAX_CONTENT_LENGTH = int(os.getenv('MAX_CONTENT_LENGTH', 5 * 1024 * 1024))  # 5 MB default
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', './uploads')


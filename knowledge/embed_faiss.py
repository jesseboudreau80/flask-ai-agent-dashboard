import os
import faiss
from dotenv import load_dotenv

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.vector_stores.faiss import FaissVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding  # ✅ Local model import

# Load environment variables from .env
load_dotenv()

# Initialize local embedding model (no API token required)
embed_model = HuggingFaceEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Apply settings globally
Settings.embed_model = embed_model

# Load parsed documents from local directory
documents = SimpleDirectoryReader("knowledge/knowledge_base").load_data()

# Determine embedding dimension
dimension = len(embed_model.get_text_embedding("test string"))

# Create FAISS index
faiss_index = faiss.IndexFlatL2(dimension)
vector_store = FaissVectorStore(faiss_index=faiss_index)

# Create and save vector index
index = VectorStoreIndex.from_documents(documents, vector_store=vector_store)
index.storage_context.persist(persist_dir="knowledge/storage")

print("✅ FAISS index created and saved to 'knowledge/storage'")

import os
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
from chromadb.utils import embedding_functions

# ✅ Explicit DuckDB config with persistence directory
settings = Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="./chroma_data"  # or any other subfolder
)

client = chromadb.Client(settings)
collection = client.get_or_create_collection(name="sop_knowledge")

model = SentenceTransformer("all-MiniLM-L6-v2")
embed_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

# Load and embed all .txt documents
source_dir = "knowledge/parsed_text"
for filename in os.listdir(source_dir):
    if filename.endswith(".txt"):
        with open(os.path.join(source_dir, filename), "r", encoding="utf-8") as f:
            content = f.read()

        collection.add(
            documents=[content],
            metadatas=[{"source": filename}],
            ids=[filename]
        )

print("✅ Embedded all SOPs into DuckDB-backed ChromaDB.")

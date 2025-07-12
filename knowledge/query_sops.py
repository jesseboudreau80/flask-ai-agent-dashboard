import os
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.llms.openai import OpenAI
from llama_index.core.retrievers import VectorIndexRetriever

# Set your OpenRouter API key (can use free models like 'mistralai/mixtral')
os.environ["OPENAI_API_KEY"] = "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"  # Replace with your OpenRouter key

# ✅ Load saved FAISS index
storage_context = StorageContext.from_defaults(persist_dir="faiss_index")
index = load_index_from_storage(storage_context)

# ✅ Setup retriever + query engine
retriever = VectorIndexRetriever(index=index)
query_engine = RetrieverQueryEngine.from_args(retriever=retriever, llm=OpenAI(model="mistralai/mixtral-8x7b"))

# 🧪 Loop for interactive questions
print("💬 Ask me anything about your SOPs (type 'exit' to quit):\n")
while True:
    query = input("🔍 You: ")
    if query.lower() in ["exit", "quit"]:
        break

    response = query_engine.query(query)
    print(f"\n📘 Answer:\n{response}\n")

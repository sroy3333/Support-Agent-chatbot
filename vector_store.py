import os
import chromadb
from langchain.embeddings.openai import OpenAIEmbeddings
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

# Load OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "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")  # Fallback if not set

# Initialize OpenAI Embeddings
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

# Initialize ChromaDB client
chroma_client = chromadb.PersistentClient(path="./vector_db")

# Ensure collection exists
if "cdp_docs" not in [c.name for c in chroma_client.list_collections()]:
    vector_store = chroma_client.create_collection("cdp_docs")
else:
    vector_store = chroma_client.get_collection("cdp_docs")

def add_to_vector_store():
    for cdp in ["segment", "mparticle", "lytics", "zeotap"]:
        file_path = f"data/{cdp}.txt"
        
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                doc_text = f.read()
            
            # Convert doc to embedding
            embedding = embeddings.embed_query(doc_text)
            
            # Store in vector database
            vector_store.add(ids=[cdp], embeddings=[embedding], metadatas=[{"text": doc_text}])
        else:
            print(f"Warning: {file_path} not found. Skipping...")

if __name__ == "__main__":
    add_to_vector_store()
    print("Vector store initialized.")


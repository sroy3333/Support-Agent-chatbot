import chromadb

chroma_client = chromadb.PersistentClient(path="./vector_db")
vector_store = chroma_client.get_collection("cdp_docs")

def retrieve_answer(query):
    docs = vector_store.query(query_texts=[query], n_results=1)
    return docs["metadatas"][0]["text"] if docs else "No relevant information found."

def compare_cdps(cdp1, cdp2):
    doc1 = retrieve_answer(f"What is {cdp1}?")
    doc2 = retrieve_answer(f"What is {cdp2}?")

    return f"Comparison of {cdp1} and {cdp2}:\n{doc1}\n\n{doc2}"
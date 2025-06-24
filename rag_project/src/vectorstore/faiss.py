from langchain_community.vectorstores import FAISS
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from rag_project.config import settings

def create_vector_index(docs, embedder):
    """
    Create a FAISS vector index from the provided documents using the specified embeddings.
    
    Args:
        embeddings: The embeddings model to use for vectorization.
        documents: A list of documents to be indexed.
        
    Returns:
        A VectorStoreIndexWrapper containing the FAISS index.
    """
    # Create a FAISS vector store with the provided embeddings and documents
    store = FAISS.from_documents(embedding=embedder, docs=docs)
    
    # Wrap the vector store in a VectorStoreIndexWrapper for easier access
    
    
    return VectorStoreIndexWrapper(vectorstore=store)
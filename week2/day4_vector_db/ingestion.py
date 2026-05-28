from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

# STEP 1 — Load text file
loader = TextLoader("sample_data.txt")

documents = loader.load()

# STEP 2 — Split into chunks
text_splitter = CharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

docs = text_splitter.split_documents(documents)

print(f"Loaded {len(docs)} chunks")

# STEP 3 — Create embeddings
embedding = OllamaEmbeddings(
    model="nomic-embed-text"
)

# STEP 4 — Store in ChromaDB
vectordb = Chroma.from_documents(
    documents=docs,
    embedding=embedding,
    persist_directory="./chroma_db"
)

print("Embeddings stored successfully in ChromaDB")
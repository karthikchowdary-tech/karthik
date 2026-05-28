from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

from langchain_ollama import OllamaLLM


# STEP 1 — Load embedding model
embedding = OllamaEmbeddings(
    model="nomic-embed-text"
)

# STEP 2 — Load existing ChromaDB
vectordb = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embedding
)

# STEP 3 — Create retriever
retriever = vectordb.as_retriever(search_kwargs={"k": 3})

# STEP 4 — Load TinyLlama
llm = OllamaLLM(
    model="tinyllama"
)


# STEP 5 — Chat loop
while True:

    question = input("\nAsk Question: ")

    if question.lower() == "exit":
        break

    response = llm.invoke(
        question
    )

    print("\nAnswer:")
    print(response)
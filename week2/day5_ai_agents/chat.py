from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import OllamaLLM

from langchain_classic.chains import RetrievalQA
from langchain_classic.memory import ConversationBufferMemory

# STEP 1 — Load embedding model
embedding = OllamaEmbeddings(
    model="nomic-embed-text"
)

# STEP 2 — Load vector database
vectordb = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embedding
)

# STEP 3 — Create retriever
retriever = vectordb.as_retriever(
    search_kwargs={"k": 3}
)

# STEP 4 — Load LLM
llm = OllamaLLM(
    model="tinyllama"
)

# STEP 5 — Add memory
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# STEP 6 — Create RetrievalQA workflow
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff"
)

print("\nAI Assistant Ready!")
print("Type 'exit' to quit.\n")

# STEP 7 — Chat loop
while True:

    question = input("You: ")

    if question.lower() == "exit":
        break

    # Multi-step reasoning prompt
    enhanced_question = f"""
    Answer step-by-step.

    Question:
    {question}
    """

    # Workflow execution
    response = qa_chain.invoke(
        {"query": enhanced_question}
    )

    answer = response["result"]

    # Save memory
    memory.save_context(
        {"input": question},
        {"output": answer}
    )

    print("\nAI:")
    print(answer)
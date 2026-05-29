from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

# STEP 1 — Load model
llm = OllamaLLM(
    model="tinyllama"
)

# STEP 2 — Create prompt
prompt = ChatPromptTemplate.from_template(
    """
    Explain the following topic simply:

    Topic: {topic}
    """
)

# STEP 3 — Create workflow chain
chain = prompt | llm

# STEP 4 — Run workflow
response = chain.invoke(
    {"topic": "Vector Databases"}
)

print("\nWorkflow Output:\n")
print(response)
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.tools import tool

from langchain_ollama import OllamaLLM

# STEP 1 — Load model
llm = OllamaLLM(
    model="tinyllama"
)

# STEP 2 — Create tools
@tool
def calculator(text: str):
    """
    Performs basic calculations.
    Example: 5 + 10
    """
    return eval(text)

@tool
def word_counter(text: str):
    """
    Counts words in text.
    """
    return len(text.split())

tools = [calculator, word_counter]

# STEP 3 — Create agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# STEP 4 — Run agent
while True:

    question = input("\nAsk Agent: ")

    if question.lower() == "exit":
        break

    response = agent.run(question)

    print("\nAgent Response:")
    print(response)
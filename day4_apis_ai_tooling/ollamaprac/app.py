import requests

while True:

    question = input("You: ")

    if question.lower() == "exit":
        break

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": question,
            "stream": False
        }
    )

    data = response.json()

    print("\nAI:", data["response"])
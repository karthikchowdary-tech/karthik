import requests

# Step 1
idea_prompt = "Give me a Python project idea"

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "tinyllama:latest",
        "prompt": idea_prompt,
        "stream": False
    }
)

idea = response.json()["response"]

# Step 2
plan_prompt = f"Create a detailed plan for: {idea}"

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "tinyllama:latest",
        "prompt": plan_prompt,
        "stream": False
    }
)

plan = response.json()["response"]

print("Project Idea:")
print(idea)

print("\nProject Plan:")
print(plan)
import requests
import json

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "tinyllama:latest",
        "prompt": "Explain Machine Learning",
        "stream": True
    },
    stream=True
)

for line in response.iter_lines():
    if line:
        data = json.loads(line)

        print(data["response"], end="")
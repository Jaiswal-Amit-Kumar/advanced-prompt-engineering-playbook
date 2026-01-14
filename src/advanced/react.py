import requests

ollama_url = 'http://localhost:11434/api/chat'

def react_prompt(question, model="phi3:latest"):
    messages = [
        {
            "role": "system",
            "content": (
                "You are an AI that uses the ReAct pattern.\n"
                "Use this format strictly:\n\n"
                "Thought:\n"
                "Action:\n"
                "Observation:\n"
                "Thought:\n"
                "Final Answer:"
            )
        },
        {
            "role": "user",
            "content": question
        }
    ]

    payload = {
        "model": model,
        "messages": messages,
        "options": {"temperature": 0.3, "num_predict": 300},
        "stream": False
    }

    r = requests.post(ollama_url, json=payload)
    r.raise_for_status()
    return r.json()["message"]["content"]

if __name__ == "__main__":
    question = "If I have 10 apples and give away 4, then buy 3 more, how many apples do I have?"
    print(react_prompt(question))


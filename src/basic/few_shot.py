import requests

ollama_url = 'http://localhost:11434/api/chat'

EXAMPLES = [
    {"input": "Translate 'Hello' to Spanish", "output": "Hola"},
    {"input": "Translate 'Goodbye' to French", "output": "Au revoir"}
]


def few_shot_query(user_input: str, examples=EXAMPLES, model="phi3:latest"):
    """Construct few-shot prompt and query model."""
    messages = [{'role':'system', 'content': 'you are an intelligent AI assistant.'}]

    for ex in examples:
        messages.append({'role':'user', 'content':ex['input']})
        messages.append({'role':'assistant', 'content': ex['output']})

    messages.append({'role':'user', 'content':user_input})
    payload = {
        'model':model,
        'messages':messages,
        'options':{'temperature': 0.0, 'num_predict': 300},
        'stream': False
    }

    response = requests.post(ollama_url, json=payload)
    response.raise_for_status()

    data = response.json()
    return data['message']['content']

if __name__ == "__main__":
    user_input = "Translate 'Thank you' to German"
    print(few_shot_query(user_input))

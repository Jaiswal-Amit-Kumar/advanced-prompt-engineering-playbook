import requests

ollama_url = 'http://localhost:11434/api/chat'

def zero_shot_query(prompt:str, model:str='phi3:latest') -> str:
    '''construct zero shot prompt and query model.'''
    payload = {
        'model':model,
        'messages':[
            {'role':'system', 'content':'You are an intelligent assistant.'},
            {'role':'user', 'content':prompt}
        ],
        'options': {
            'temperature': 0.0,
            'num_predict': 300
        },
        "stream": False
    }

    response = requests.post(ollama_url, json=payload)
    response.raise_for_status()

    data = response.json()
    return data['message']['content']

if __name__ == '__main__':
    prompt = 'Summarize AI trends in 3 bullet points.'
    print(zero_shot_query(prompt))
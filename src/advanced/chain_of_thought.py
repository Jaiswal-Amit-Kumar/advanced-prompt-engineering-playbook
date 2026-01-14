import requests

ollama_url = 'http://localhost:11434/api/chat'

def chain_of_thought_query(user_input: str, model: str='phi3:latest') -> str:
    '''chain of thought agent helping with mathmatical and reasoninng querries'''
    messages = [
        {'role':'system', 'content':'You are an intelligent AI assistent build for chain of thought tasks.'},
        {'role':'user', 'content': f'{question}, \n please explain step by step reasoning for the question provided.'}
    ]

    payload = {
        'model':model,
        'messages':messages,
        'options':{'temperature':0.0, 'num_predict': 300},
        'stream': False
    }

    response = requests.post(ollama_url, json=payload)
    response.raise_for_status()

    data = response.json()

    return data['message']['content']

if __name__=='__main__':
    question = 'If I have 5 apples and buy 3 more, how many do I have in total?'
    print(chain_of_thought_query(question))
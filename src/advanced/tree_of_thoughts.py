import requests

ollama_url = 'http://localhost:11434/api/chat'

def tree_of_thought(user_input:str, model:str='phi3:latest') -> str:
    '''tree of thought agent helping in branching technique'''

    messages=[
        {'role':'system', 'content':('''You are a careful and intelligent AI assistant. 
            For the following problem, think of multiple possible reasoning paths (branches), 
            explore each path step by step, and then choose the best final answer.'''
        )},
        {'role':'user', 'content':f'{question},\n please think in a tree of thought format and give the best final answer.'}
    ]

    payload = {
        'model':model,
        'messages':messages,
        'options':{'temperature':0.0, 'num_predict':300},
        'stream': False
    }

    response = requests.post(ollama_url, json=payload)
    response.raise_for_status()

    data = response.json()
    return data['message']['content']

if __name__ == '__main__':
    question = 'If I have 5 apples and buy 3 more, how many do I have in total?'
    print(tree_of_thought(question))
import requests

ollama_url = 'http://localhost:11434/api/chat'

def call_ollama_for_every_prompt(messages, model:str='phi3:latest') -> str:
    '''calling ollama model for every prompt in chain'''
    payload = {
        'model':model,
        'messages': messages,
        'options':{'temperature': 0.0, 'num_pridict': 300},
        'stream': False
    }

    response = requests.post(ollama_url, json=payload)
    response.raise_for_status()

    data = response.json()
    return data['message']['content']

def prompt_chaining(question):

    '''understand the problem'''
    messages_step1 = [
        {'role':'system', 'content':'You are an AI that summarizes problems clearly.'},
        {'role':'user', 'content':f'explain this queation as what is asked \n {question}'}
    ]

    understanding = call_ollama_for_every_prompt(messages_step1)

    '''reason the problem'''
    messages_step2 = [
        {'role':'system', 'content':'You are an AI that reasons step by step.'},
        {'role':'user', 'content':f'Problem understanding:\n{understanding}\n\nSolve it step by step.'}
    ]

    reasoning = call_ollama_for_every_prompt(messages_step2)

    '''final answer only'''

    messages_step3 = [
        {'role':'system', 'content':'Give only the final answer, no explanation.'},
        {'role':'user', 'content':f'provide the final answer{reasoning}'}
    ]

    final_answer = call_ollama_for_every_prompt(messages_step3)

    return {
        'understanding': understanding,
        'reasoning': reasoning,
        'final_answer': final_answer
    }

if __name__ == '__main__':
    question = 'If I have 10 apples and give away 4, then buy 3 more, how many apples do I have?'
    result = prompt_chaining(question)

    print('understanding\n', result['understanding'])
    print('reasoning\n', result['reasoning'])
    print('final_answer\n', result['final_answer'])
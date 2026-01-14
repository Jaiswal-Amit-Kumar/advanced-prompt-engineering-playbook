import requests
import re

OLLAMA_URL = "http://localhost:11434/api/chat"

def pal_prompt(question, model="phi3:latest"):
    '''PAL Prompting (Program-Aided Language)
    PAL = Let the model write code to solve the problem, instead of reasoning only in text.

👉 The model:

Understands the problem

Writes a small Python program

Uses the program to get the correct answer

This is very powerful for math, logic, counting, and rules.'''
    messages = [
        {
            "role": "system",
            "content": (
                "You are an AI that solves problems by writing Python code. "
                "Only write valid Python code. Do not explain anything."
                "Do not use markdown. Do not use ```."

            )
        },
        {
            "role": "user",
            "content": f"""
Solve the following problem by writing Python code.

Problem:
{question}

Rules:
- Only output Python code
- Store the final answer in a variable called `result`
"""
        }
    ]

    payload = {
        "model": model,
        "messages": messages,
        "options": {"temperature": 0.0, "num_predict": 200},
        "stream": False
    }

    r = requests.post(OLLAMA_URL, json=payload)
    r.raise_for_status()

    code = r.json()["message"]["content"]
    return code

import re

def clean_python_code(code: str) -> str:
    """
    Removes markdown code fences like ```python ... ```
    """
    code = re.sub(r"```python", "", code)
    code = re.sub(r"```", "", code)
    return code.strip()


def execute_pal_code(code):
    local_vars = {}
    clean_code = clean_python_code(code)
    exec(clean_code, {}, local_vars)
    return local_vars.get("result")



if __name__ == "__main__":
    question = "If I have 5 apples and buy 3 more, how many apples do I have?"

    code = pal_prompt(question)
    print("GENERATED CODE:\n", code)

    answer = execute_pal_code(code)
    print("FINAL ANSWER:", answer)

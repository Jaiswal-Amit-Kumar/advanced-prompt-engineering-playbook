import requests
import re
from collections import Counter

OLLAMA_URL = "http://localhost:11434/api/chat"

def extract_final_answer(text):
    patterns = [
        r"FINAL\s*ANSWER\s*[:\-]\s*<?\s*(\d+)\s*>?",
        r"Final\s*Answer\s*[:\-]\s*(\d+)",
        r"Answer\s*[:\-]\s*(\d+)"
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1)
    return None


def self_consistency(question, runs=5, model="phi3:latest"):
    answers = []

    for _ in range(runs):
        messages = [
            {"role": "system", "content": "You are an AI that reasons step by step."},
            {"role": "user", "content": (
                f"{question}\n"
                "Explain your reasoning step by step.\n"
                "On the last line, write:\n"
                "FINAL ANSWER: <number>"
            )}
        ]

        payload = {
            "model": model,
            "messages": messages,
            "options": {"temperature": 0.7, "num_predict": 200},
            "stream": False
        }

        r = requests.post(OLLAMA_URL, json=payload)
        r.raise_for_status()
        output = r.json()["message"]["content"]

        answer = extract_final_answer(output)
        if answer:
            answers.append(answer)

    if not answers:
        raise ValueError("No valid answers extracted from model outputs.")

    most_common_answer = Counter(answers).most_common(1)[0][0]

    return {
        "all_answers": answers,
        "final_answer": most_common_answer
    }


if __name__ == '__main__':
    question = 'If I have 5 apples and buy 3 more, how many apples do I have?'
    result = self_consistency(question)

    print('all answers:')
    for a in result['all_answers']:
        print('-',a)

    print('\nfinal (most consistent) answer:')
    print(result['final_answer'])

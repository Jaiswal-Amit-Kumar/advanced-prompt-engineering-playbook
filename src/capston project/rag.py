import requests
import re
from collections import Counter

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "phi3:latest"


DOCUMENTS = [
    "Apples are fruits. One apple has about 95 calories.",
    "Buying items increases total count. Giving away items decreases total count.",
    "Buying items increases total count. Giving away items decreases total count.",
    "Buying items increases total count. Giving away items decreases total count.",
    "Basic arithmetic: addition increases values, subtraction decreases values.",
    "A basket initially has apples, and transactions change the quantity."
]

def retrieve_docs(question, docs, k=2):
    scored = []
    for doc in docs:
        score = sum(word.lower() in doc.lower() for word in question.split())
        scored.append((score, doc))
    scored.sort(reverse=True)
    return [doc for _, doc in scored[:k]]

def call_ollama(messages, temperature=0.0, max_tokens=300):
    payload = {
        "model": MODEL,
        "messages": messages,
        "options": {"temperature": temperature, "num_predict": max_tokens},
        "stream": False
    }
    r = requests.post(OLLAMA_URL, json=payload)
    r.raise_for_status()
    return r.json()["message"]["content"]

def reasoning_step(question, context):
    messages = [
        {
            "role": "system",
            "content": (
                "You are a careful AI that answers questions using the provided context.\n"
                "Think step by step before answering."
            )
        },
        {
            "role": "user",
            "content": (
                f"Context:\n{context}\n\n"
                f"Question:\n{question}\n\n"
                "Explain your reasoning step by step.\n"
                "End with: FINAL ANSWER: <number>"
            )
        }
    ]
    return call_ollama(messages, temperature=0.3)


def extract_answer(text):
    match = re.search(r"FINAL\s*ANSWER\s*:\s*<?(\d+)>?", text, re.IGNORECASE)
    return match.group(1) if match else None


def self_consistent_reasoning(question, context, runs=5):
    answers = []

    for _ in range(runs):
        output = reasoning_step(question, context)
        answer = extract_answer(output)
        if answer:
            answers.append(answer)

    if not answers:
        raise ValueError("No valid answers extracted")

    final = Counter(answers).most_common(1)[0][0]
    return final, answers

def pal_verify(answer):
    try:
        return int(answer)
    except:
        return None
    
def rag_pipeline(question):
    # 1. Retrieve
    retrieved_docs = retrieve_docs(question, DOCUMENTS)
    context = "\n".join(retrieved_docs)

    # 2. Reason + self-consistency
    final_answer, all_answers = self_consistent_reasoning(question, context)

    # 3. Optional PAL verification
    verified = pal_verify(final_answer)

    return {
        "question": question,
        "retrieved_docs": retrieved_docs,
        "all_answers": all_answers,
        "final_answer": verified
    }

if __name__ == "__main__":
    question = "If I have 5 apples and buy 3 more, how many apples do I have?"

    result = rag_pipeline(question)

    print("QUESTION:", result["question"])
    print("\nRETRIEVED DOCUMENTS:")
    for d in result["retrieved_docs"]:
        print("-", d)

    print("\nALL ANSWERS:", result["all_answers"])
    print("\nFINAL ANSWER:", result["final_answer"])

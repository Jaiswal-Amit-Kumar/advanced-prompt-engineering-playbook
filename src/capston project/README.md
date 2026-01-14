# Capstone Project: Advanced Reasoning with LLMs (Chain-of-Thought, Tree-of-Thought & RAG)

This is a **capstone project** demonstrating **advanced reasoning and retrieval techniques for large language models (LLMs)**.  
The project combines **Retrieval-Augmented Generation (RAG)** with **Chain-of-Thought (CoT)** and **Tree-of-Thought (ToT)** reasoning paradigms, showcasing **multi-step reasoning, consistency verification, and programmatic problem-solving**.

It is designed to highlight both **technical skills in AI/LLMs** and **problem-solving workflows**, making it suitable for **portfolio demonstration or recruiter review**.

---

## Project Overview

Modern LLMs are powerful but can produce **inconsistent or ungrounded outputs**. This project addresses these challenges by:

1. **Retrieving relevant context** from a set of documents (RAG).  
2. **Performing step-by-step reasoning** using Chain-of-Thought (CoT).  
3. **Exploring multiple reasoning branches** using Tree-of-Thought (ToT) for better solution quality.  
4. **Self-consistency checks** to select the most reliable answer.  
5. **Optional PAL verification**, executing Python code to validate numerical answers.

---

## Key Components

### 1. Retrieval-Augmented Generation (RAG)
- **Function:** `retrieve_docs(question, docs, k=2)`  
- **Purpose:** Selects the most relevant documents from a knowledge base to provide grounded context for reasoning.  
- **Example:**
```python
retrieved_docs = retrieve_docs("How many apples after buying 3 more?", DOCUMENTS)
````

### 2. Chain-of-Thought Reasoning (CoT)

* **Function:** `reasoning_step(question, context)`
* **Purpose:** Guides the model to reason **step-by-step** instead of giving an immediate answer, improving correctness in math, logic, and counting tasks.

### 3. Self-Consistency

* **Function:** `self_consistent_reasoning(question, context, runs=5)`
* **Purpose:** Queries the model multiple times and returns the **most frequent final answer**, reducing errors due to stochastic outputs.

### 4. Tree-of-Thought Reasoning (ToT)

* **Concept:** Explores **multiple reasoning branches**, evaluates each path, and selects the **best final answer**.
* **Purpose:** Increases solution quality for complex or ambiguous problems by considering alternate reasoning paths.

### 5. Program-Aided Verification (PAL)

* **Function:** `pal_verify(answer)`
* **Purpose:** Optionally validates numeric answers by executing Python code if applicable.

---

## Capstone Pipeline: `rag_pipeline(question)`

1. **Retrieve** top-k relevant documents.
2. **Reason** step-by-step with CoT.
3. **Run self-consistency** to choose the most reliable answer.
4. **Optional PAL verification** for numeric correctness.
5. **Return structured output** with retrieved docs, all intermediate answers, and final verified answer.

**Example usage:**

```python
from capstone_pipeline import rag_pipeline

question = "If I have 5 apples and buy 3 more, how many apples do I have?"
result = rag_pipeline(question)

print("QUESTION:", result["question"])
print("\nRETRIEVED DOCUMENTS:", result["retrieved_docs"])
print("\nALL ANSWERS:", result["all_answers"])
print("\nFINAL ANSWER:", result["final_answer"])
```

---

## Key Features & Highlights

* **Advanced reasoning techniques:** CoT and ToT implemented for multi-step problem solving.
* **Grounded answers:** RAG ensures reasoning is based on relevant documents.
* **Consistency and reliability:** Self-consistency reduces errors across multiple runs.
* **Programmatic validation:** Optional PAL verification of numeric answers.
* **Modular and reusable:** Each component can be integrated into other projects or notebooks.

---

## Why Recruiters Should Care

This capstone demonstrates:

* **Expertise in LLM reasoning workflows** (CoT, ToT, RAG, PAL).
* **Ability to design and implement multi-step AI pipelines**.
* **Data-driven problem-solving skills** with retrieval and verification.
* **Modular and well-structured Python code**, suitable for production-level AI projects.

This project is **portfolio-ready** and highlights both **technical depth and practical AI skills**, making it highly relevant for **AI/ML engineering, research, or LLM-focused roles**.

---

## Getting Started

1. **Install dependencies**:

```bash
pip install requests
```

2. **Ensure LLM server is running** locally at `http://localhost:11434` (Ollama).

3. **Run the capstone pipeline**:

```bash
python capstone_pipeline.py
```

4. **Modify `DOCUMENTS` or `question`** to experiment with new reasoning tasks.

```
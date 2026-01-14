# Prompt Engineering Playbook

A **comprehensive, personal project** showcasing advanced prompt engineering techniques for large language models (LLMs).  
This repository combines **educational content, practical implementations, experiments, and datasets** to demonstrate state-of-the-art prompting strategies, reasoning methods, and retrieval-augmented generation.

This project serves as both a **portfolio piece** and a **learning resource** for LLM applications.

---

## Project Overview

**Prompt engineering** is the art of designing input prompts that maximize the reasoning, creativity, and accuracy of AI language models.  
In this project, I explore and implement a variety of techniques, ranging from foundational prompting to advanced multi-step reasoning:

- **Basic Prompting**: Zero-shot, few-shot, and role-based prompts to guide the model effectively.  
- **Advanced Reasoning**: Chain-of-thought, self-consistency, tree-of-thought, ReAct, and Program-Aided Language (PAL) models.  
- **Retrieval-Augmented Generation (RAG)**: Combining external knowledge sources with LLM outputs to reduce hallucinations and improve grounding.

This project demonstrates **clean coding practices, modular structure, and reproducible experiments**, highlighting my ability to work on complex AI workflows.

---

## Folder Structure

- `src/` → Core implementations of prompt engineering techniques
  - `basic/` → Zero-shot, few-shot, and role-based prompting implementations
  - `advanced/` → Chain-of-thought, self-consistency, tree-of-thought, ReAct, PAL, RAG
  - `utils/` → Helper functions, reusable templates, and evaluation scripts

- `notebooks/` → Interactive Jupyter notebooks for demonstrations, tutorials, and experiments
  - `01_basic_prompting.ipynb` → Zero-shot and few-shot prompting tutorials
  - `02_advanced_reasoning.ipynb` → Advanced reasoning, chain-of-thought, and self-consistency experiments
  - `03_rag_examples.ipynb` → Retrieval-augmented generation (RAG) and grounding experiments

- `data/` → Datasets used for demonstrations and experiments
  - `faq_dataset.json` → Sample FAQ dataset for RAG experiments

- `docs/` → Documentation and conceptual explanations
  - `techniques.md` → Detailed descriptions of all techniques, their advantages, and use cases

---

## Key Features & Highlights

- **Portfolio-Ready Implementations**: Clean, modular, and well-documented code suitable for demonstration to recruiters.  
- **Educational Notebooks**: Step-by-step tutorials and experiments for hands-on learning.  
- **Advanced Reasoning Techniques**: Includes chain-of-thought, self-consistency, tree-of-thought, and program-aided reasoning.  
- **Grounded AI Outputs**: RAG-based experiments to reduce hallucinations and improve answer accuracy.  
- **Skill Demonstration**: Highlights Python programming, LLM reasoning, prompt design, and experimental methodology.

---

## Getting Started

Follow these steps to explore the repository:

1. **Create and activate a Python environment**:
```bash
python -m venv env
# macOS / Linux
source env/bin/activate
# Windows
env\Scripts\activate
pip install -r requirements.txt
````

2. **Explore notebooks**: Open the Jupyter notebooks in `notebooks/` to run tutorials and experiments interactively.

3. **Run the source code directly**:

```python
from src.basic.zero_shot import zero_shot_prompt

question = "Explain the water cycle in simple terms."
print(zero_shot_prompt(question))
```

4. **Use datasets**: Load `data/faq_dataset.json` for RAG experiments or extend with your own examples for testing prompts.

---

## Why This Project Matters to Recruiters

This project demonstrates:

* **Technical Expertise**: Understanding of advanced LLM prompting techniques and reasoning methods.
* **Code Organization & Best Practices**: Clear modular structure, reusable functions, and maintainable code.
* **Problem-Solving Skills**: Implementing complex reasoning workflows and integrating data-driven approaches.
* **Educational Ability**: Clear explanations and tutorials, showing ability to communicate complex ideas.

It is designed to **showcase both technical skills and thought process**, which is highly valued in AI/ML and LLM-focused roles.

---

## Personal Notes

* This is a **self-initiated project**; all implementations, notebooks, and datasets were created by me.
* It is intended to serve as a **portfolio demonstration** of my skills in AI prompt engineering and reasoning.

---
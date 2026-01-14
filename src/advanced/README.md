# Advanced Prompting Techniques

This folder contains **advanced prompt engineering and reasoning techniques** for large language models (LLMs).  
These implementations go beyond basic zero-shot and few-shot prompting to include **multi-step reasoning, program-aided problem solving, tree-based exploration, self-consistency, and ReAct workflows**.  

These techniques demonstrate **complex reasoning, logical problem solving, and modular AI workflows**, highlighting skills in both AI experimentation and software engineering.

---

## Files and Techniques

### `chain_of_thought.py`
- Implements **Chain-of-Thought prompting**, where the model explains its reasoning step by step.
- **Key function:** `chain_of_thought_query(user_input: str, model: str = 'phi3:latest') -> str`
- **Purpose:** Improves accuracy in math, logic, and reasoning tasks by making the model "think aloud."
- **Example usage:**
```python
from src.advanced.chain_of_thought import chain_of_thought_query

question = "If I have 5 apples and buy 3 more, how many apples do I have?"
answer = chain_of_thought_query(question)
print(answer)
````

---

### `pal.py`

* Implements **Program-Aided Language (PAL)** prompting.
* **Key functions:**

  * `pal_prompt(question)` → Generates Python code to solve the problem.
  * `execute_pal_code(code)` → Executes generated code and retrieves the final answer.
* **Purpose:** Lets the model **write and execute code** to solve logic, math, or counting problems.
* **Example usage:**

```python
from src.advanced.pal import pal_prompt, execute_pal_code

question = "If I have 5 apples and buy 3 more, how many apples do I have?"
code = pal_prompt(question)
answer = execute_pal_code(code)
print("Final Answer:", answer)
```

---

### `prompt_chaining.py`

* Implements **Prompt Chaining**, splitting reasoning into multiple steps:

  1. Problem understanding
  2. Step-by-step reasoning
  3. Final answer extraction
* **Key function:** `prompt_chaining(question)` → Returns a dictionary with `understanding`, `reasoning`, and `final_answer`.
* **Purpose:** Demonstrates modular reasoning workflows suitable for complex multi-step tasks.

---

### `react.py`

* Implements **ReAct prompting**:

  * **Thought → Action → Observation → Thought → Final Answer**
* **Key function:** `react_prompt(question, model='phi3:latest')`
* **Purpose:** Combines reasoning with action-taking steps, useful for interactive or sequential tasks.

---

### `tree_of_thought.py`

* Implements **Tree-of-Thought prompting**, where the model explores multiple reasoning branches.
* **Key function:** `tree_of_thought(user_input: str, model: str = 'phi3:latest') -> str`
* **Purpose:** Enhances solution quality by exploring multiple reasoning paths and selecting the best final answer.

---

### `self_consistency.py`

* Implements **Self-Consistency** reasoning:

  * Queries the model multiple times.
  * Extracts answers from each run.
  * Returns the **most consistent final answer**.
* **Key function:** `self_consistency(question, runs=5, model='phi3:latest')`
* **Purpose:** Reduces errors and improves reliability in tasks requiring exact answers.

---

## Key Features

* **Multi-step reasoning workflows**: Chain-of-thought, tree-of-thought, prompt chaining.
* **Programmatic problem solving**: PAL allows models to generate and execute code.
* **Action-oriented AI workflows**: ReAct combines reasoning with sequential actions.
* **Consistency and reliability**: Self-consistency ensures robust answers across multiple runs.
* **Modular & reusable code**: Each technique can be imported into notebooks or integrated into larger pipelines.

---

## How to Use

1. **Install requirements**:

```bash
pip install requests
```

2. **Ensure Ollama LLM API is running** locally at `http://localhost:11434`.

3. **Import and test any technique**:

```python
from src.advanced.chain_of_thought import chain_of_thought_query
from src.advanced.pal import pal_prompt, execute_pal_code

question = "If I have 5 apples and buy 3 more, how many apples do I have?"
answer = chain_of_thought_query(question)
print(answer)

code = pal_prompt(question)
result = execute_pal_code(code)
print(result)
```

4. **Experiment with other techniques**: `prompt_chaining`, `react`, `tree_of_thought`, `self_consistency`.

---

## Notes for Recruiters

This folder demonstrates:

* **Expertise in advanced LLM prompting techniques**.
* **Ability to implement complex reasoning workflows** for AI models.
* **Modular Python code and pipeline design**, showcasing production-ready skills.
* **Analytical and problem-solving mindset** through chain-of-thought, self-consistency, and PAL techniques.

These skills are **directly relevant for AI/ML roles**, research positions, and LLM-focused engineering tasks.

```
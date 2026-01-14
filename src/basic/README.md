# Basic Prompting Techniques

This folder contains **fundamental prompt engineering implementations** for large language models (LLMs), focusing on **zero-shot** and **few-shot prompting** strategies.  
These techniques form the foundation for more advanced reasoning and multi-step prompting workflows.

---

## Files and Functions

### `zero_shot.py`
- Implements **zero-shot prompting**, where the model is given a task without any examples.
- **Key function:** `zero_shot_query(prompt: str, model: str = 'phi3:latest') -> str`
  - Sends a single prompt to the model.
  - Returns the model's response.
- **Example usage:**
```python
from src.basic.zero_shot import zero_shot_query

prompt = "Summarize AI trends in 3 bullet points."
response = zero_shot_query(prompt)
print(response)
````

### `few_shot.py`

* Implements **few-shot prompting**, where a small set of input-output examples are provided to guide the model.
* **Key function:** `few_shot_query(user_input: str, examples: list = EXAMPLES, model: str = 'phi3:latest') -> str`

  * Automatically constructs a few-shot prompt from predefined examples.
  * Queries the model and returns its response.
* **Example usage:**

```python
from src.basic.few_shot import few_shot_query

user_input = "Translate 'Thank you' to German"
response = few_shot_query(user_input)
print(response)
```

* **Default examples** demonstrate simple translations like:

  * `"Translate 'Hello' to Spanish"` → `"Hola"`
  * `"Translate 'Goodbye' to French"` → `"Au revoir"`

---

## Key Features

* **Zero-shot prompting:** Quick and simple for tasks where the model has prior knowledge.
* **Few-shot prompting:** Guides the model using examples to improve accuracy and output style.
* **Reusable functions:** Modular design for integrating into larger pipelines or experiments.
* **Local LLM support:** Works with an Ollama local API (`http://localhost:11434`) for fast and private testing.

---

## How to Use

1. **Install requirements** if not already installed:

```bash
pip install requests
```

2. **Ensure your LLM server is running locally** on port `11434` (Ollama).

3. **Run zero-shot or few-shot queries**:

```bash
python zero_shot.py
python few_shot.py
```

4. **Integrate functions** into notebooks or advanced experiments by importing:

```python
from src.basic.zero_shot import zero_shot_query
from src.basic.few_shot import few_shot_query
```

---

## Notes for Recruiters

This folder demonstrates:

* **Core understanding of prompt engineering paradigms** (zero-shot vs few-shot).
* **Ability to structure prompts effectively** for LLMs.
* **Modular, reusable Python code** suitable for both experiments and production-level pipelines.

These are foundational skills for AI/ML roles involving LLM deployment, experimentation, and evaluation.

```
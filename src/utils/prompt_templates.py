ZERO_SHOT_TEMPLATE = "Answer the following question clearly and concisely:\n{question}"

FEW_SHOT_TEMPLATE = """
You are a helpful assistant. Follow these examples:
{examples}

Now respond to the following:
Input: {user_input}
Output:
"""

CHAIN_OF_THOUGHT_TEMPLATE = "Think step-by-step to solve:\n{problem}"

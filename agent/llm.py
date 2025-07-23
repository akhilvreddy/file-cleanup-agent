import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")
import re
import ast

def generate_plan(prompt):
    print("\n Sending prompt to LLM...\n")
    print(prompt[:1000] + "...\n")  # truncated prompt

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    content = response['choices'][0]['message']['content']
    print("LLM Response:\n", content)
    cleaned = extract_code_block(content)
    return ast.literal_eval(cleaned)  # list of function calls as strings

def extract_code_block(text):
    match = re.search(r"```python(.*?)```", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return text.strip()
import openai

def generate_plan(prompt):
    print("\n📤 Sending prompt to LLM...\n")
    print(prompt[:1000] + "...\n")  # truncated prompt

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    content = response['choices'][0]['message']['content']
    print("📥 LLM Response:\n", content)
    return eval(content)  # list of function calls as strings
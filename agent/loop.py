import time
from agent.actions import get_directory_state, execute_action
from agent.llm import generate_plan
from agent.memory import AgentMemory
from agent.prompt_builder import build_prompt

def run_agent(target_dir, dry_run=True, max_steps=1):
    memory = AgentMemory()
    step = 0

    while step < max_steps:
        print(f"\n=== Agent Step {step + 1} ===")

        state = get_directory_state(target_dir)

        prompt = build_prompt(state, memory, dry_run=dry_run)

        actions = generate_plan(prompt)

        for action in actions:
            result = execute_action(action, dry_run=dry_run)
            memory.update(action, result)

        step += 1
        time.sleep(1)

    print("\n Cleanup complete.")
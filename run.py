from agent.loop import run_agent

if __name__ == "__main__":
    run_agent(target_dir="examples/messy-dataset", dry_run=True, max_steps=1)
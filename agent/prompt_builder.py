def build_prompt(state, memory, dry_run=False):
    base = open("prompts/base_prompt.txt").read()

    state_str = "\n".join([
        f'{{ "name": "{f["name"]}", "size": "{f["size"]}", "modified": "{f["modified"]}" }}'
        for f in state
    ])

    memory_str = "\n".join([
        f"# {a} -> {r}" for a, r in memory.action_log
    ])

    dry_prefix = "Current mode: dry run\n" if dry_run else ""

    return f"""{base}

{dry_prefix}

Current Directory Snapshot:
[
{state_str}
]

Past Actions:
{memory_str}
"""
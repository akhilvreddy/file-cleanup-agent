import os
import shutil

def get_directory_state(path):
    files = []
    for name in os.listdir(path):
        full_path = os.path.join(path, name)
        try:
            stats = os.stat(full_path)
            files.append({
                "name": name,
                "size": stats.st_size,
                "modified": stats.st_mtime,
                "path": full_path
            })
        except Exception as e:
            files.append({
                "name": name,
                "error": str(e)
            })
    return files

def execute_action(action_str, dry_run=True):
    try:
        if dry_run:
            return f"[DRY RUN] Would execute: {action_str}"

        func_name = action_str.split("(", 1)[0]
        args = eval("[" + action_str.split("(", 1)[1])  # like move_file("a", "b")

        if func_name == "create_folder":
            return create_folder(*args)
        elif func_name == "move_file":
            return move_file(*args)
        elif func_name == "delete_file":
            return delete_file(*args)
        else:
            return f"[ERROR] Unknown action: {action_str}"

    except Exception as e:
        return f"[ERROR] {action_str} → {str(e)}"

def create_folder(path):
    os.makedirs(path, exist_ok=True)
    return f"Created folder: {path}"

def move_file(src, dst):
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.move(src, dst)
    return f"Moved {src} → {dst}"

def delete_file(path):
    if os.path.exists(path):
        os.remove(path)
        return f"Deleted: {path}"
    return f"[WARNING] File not found: {path}"
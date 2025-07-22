import sys

# downloading outside docker
from datasets import load_dataset

def clone_dataset_cache():
    dataset = load_dataset("akhilvreddy/simple-linux-containerized-dataset")

# downloading inside docker
import os
import shutil

def clone_and_extract_messy_dataset():
    repo_name = "simple-linux-containerized-dataset"
    messy_folder = os.path.join(repo_name, "messy-dataset")
    target_folder = "messy-dataset"

    if not os.path.exists(target_folder):
        print("Cloning Hugging Face dataset repo...")
        os.system(f"git clone https://huggingface.co/datasets/akhilvreddy/{repo_name}")

        if not os.path.exists(messy_folder):
            raise FileNotFoundError("Expected messy-dataset/ folder not found inside cloned repo.")

        print("Moving messy-dataset/ to project root...")
        shutil.move(messy_folder, target_folder)

        print("Cleaning up cloned repo...")
        shutil.rmtree(repo_name)

        print("messy-dataset/ is now at project root.")
    else:
        print("messy-dataset/ already exists — skipping clone.")


if __name__ == "__main__": 
    if len(sys.argv) != 2:
        print("Usage: python generate_data.py [local OR docker]")
        sys.exit(1)

    if sys.argv[1] == "local":
        clone_dataset_cache()

    elif sys.argv[1] == "docker":
        clone_and_extract_messy_dataset()

    else:
        print("Invalid argument. Use 'local' or 'docker'.")
        sys.exit(1)
#!/usr/bin/env python3

import time
import subprocess

subprocess.run(["python", "data/generate_data.py", "docker"], check=True)

time.sleep(3)

print("Dataset clone successful. Starting our agent now.")

# subprocess.run(["python", "run.py"], check=True)
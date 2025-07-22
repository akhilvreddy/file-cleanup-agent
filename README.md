[This](https://akhilvreddy.com/posts/agentic-framework/) is the original blog post that I wrote. [This](https://huggingface.co/datasets/akhilvreddy/simple-linux-containerized-dataset) is the test dataset I am using. I hosted the dataset on hugging face and have more information about what's in it there.

---

# File Cleanup Agent

An autonomous agent that organizes a messy Linux-style file system using real system calls, reasoning via GPT-4, and a memory-driven planning loop containerized in Docker.

---

## What this does

What It Does

- Scans an unstructured file system (like `Downloads/`)
- Uses GPT-4 to reason about what files are, where they should go, and what to delete
- Takes real actions like `mv`, `mkdir`, and `rm`
- Has memory, reflexion, and a dry-run safety mode
- Runs inside a Docker container as a self-contained agent

---

## Example output

Here's what the original "dataset" looked like 

```txt
messy-dataset/
├── main.py
├── app.java
├── README
├── .DS_Store
├── notes.txt
├── temp.tmp
├── build/
│   ├── debug.log
│   ├── app.class
│   ├── old_build/
│   │   ├── unused.o
│   │   └── trace.bak
│   └── .env.local
├── data/
│   ├── dataset1.csv
│   ├── backup/
│   │   ├── dataset1_copy.csv
│   │   └── temp.csv~
│   ├── corrupted.txt
│   └── .ipynb_checkpoints/
│       └── dataset1-checkpoint.csv
├── scripts/
│   ├── hello.js
│   ├── hello.py
│   ├── hello.java
│   ├── calc.rs
│   ├── test.cpp
│   ├── .gitkeep
│   └── scratch/
│       ├── temp_script.py
│       └── notes.md
├── archive/
│   ├── 2021_old_code/
│   │   ├── unused.py
│   │   └── results.xls
│   ├── 2020_rust_proj/
│   │   ├── main.rs
│   │   ├── Cargo.toml
│   │   └── target/
│   │       └── debug/
│   │           └── rust_binary
│   └── .trash/
│       └── .hidden_file
└── misc/
    ├── dog.jpeg
    ├── resume.finalFINAL.pdf
    └── readme.txt
```

Here's a snippet of what the agent returned in "dry-run" mode
```py
print(hi)
```

And here's what the directory looked like after the cleanup

```txt
messy-dataset/
├── main.py
├── app.java
├── README
├── .DS_Store
├── notes.txt
├── temp.tmp
├── build/
│   ├── debug.log
│   ├── app.class
│   ├── old_build/
│   │   ├── unused.o
│   │   └── trace.bak
│   └── .env.local
├── data/
│   ├── dataset1.csv
│   ├── backup/
│   │   ├── dataset1_copy.csv
│   │   └── temp.csv~
│   ├── corrupted.txt
│   └── .ipynb_checkpoints/
│       └── dataset1-checkpoint.csv
├── scripts/
│   ├── hello.js
│   ├── hello.py
│   ├── hello.java
│   ├── calc.rs
│   ├── test.cpp
│   ├── .gitkeep
│   └── scratch/
│       ├── temp_script.py
│       └── notes.md
```

---

## How it works

---

## Running the agent (in docker)

```bash
./setup_agent.sh
```

This 1) Builds the Docker container and 2) Clones and prepares the dataset at the root.

Then inside of docker we can run 

```py
python run.py
```

---

## Use by yourself

You can repeat the same steps as above but you just need an LLM API key. I used OpenAI but you can use anything else that you want.

Add your API key

```bash
export OPENAI_API_KEY=yourkey
```

To run in dry run mode

```bash
python run.py --dryrun
```

else 

```bash
python run.py
```

---
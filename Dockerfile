FROM python:3.10-slim

# set working directory inside the container
WORKDIR /app

# copy full project into container
COPY . .

# we need git
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# data cloning
CMD ["python", "data/generate_data.py", "docker"]
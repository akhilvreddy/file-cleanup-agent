FROM python:3.10-slim

# set working directory inside the container
WORKDIR /app

# copy full project into container
COPY . .

# python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# data cloning
CMD ["python", "generate_data.py", "docker"]
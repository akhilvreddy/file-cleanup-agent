#!/bin/bash

echo "Building Docker image..."
docker build -t file-agent .

echo "Setting up file system in Docker..."
docker run -it -e OPENAI_API_KEY=$OPENAI_API_KEY --entrypoint /bin/bash file-agent
#!/bin/bash

echo "Building Docker image..."
docker build -t file-agent .

echo "Setting up file system in Docker..."
docker run --rm file-agent
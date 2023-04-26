#!/usr/bin/env bash

# Builds the docker image for amd64 and arm64 and pushes it to docker hub

docker buildx build --platform=linux/arm64,linux/amd64 --tag qdwight/wolvsec --push -f Dockerfile.debian .

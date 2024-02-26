#!/bin/bash

set -eo pipefail

usage() {
    echo "Usage: $0 [OPTIONS]"
    echo "Options:"
    echo "  -p, --DOCKERFILE_PATH"
    echo "  -r, --DOCKERHUB_REPOSITORY"
    echo "  -u, --DOCKERHUB_USER"
    echo "  -t, --DOCKERHUB_TOKEN"
    echo "  -T, --TAG"
    exit 1
}

DOCKERFILE_PATH="../.."
DOCKERHUB_REPOSITORY=""
DOCKERHUB_USER=""
DOCKERHUB_TOKEN=""
TAG="latest"

# Check args
while [[ $# -gt 0 ]]; do
    key="$1"
    case $key in
        -p)
            DOCKERFILE_PATH="$2"
            shift 2
        ;;
        -r)
            DOCKERHUB_REPOSITORY="$2"
            shift 2
        ;;
        -u)
            DOCKERHUB_USER="$2"
            shift 2
        ;;
        -t)
            DOCKERHUB_TOKEN="$2"
            shift 2
        ;;
        -T)
            TAG="$2"
            shift 2
        ;;
        *)
            usage
        ;;
    esac
done

# Check if required arguments are provided
if [ -z "$DOCKERFILE_PATH" ] || [ -z "$DOCKERHUB_REPOSITORY" ] || [ -z "$DOCKERHUB_USER" ]; then
    echo "Error: Missing required arguments."
    usage
fi
echo "ee"
echo "Docker file path is ${DOCKERFILE_PATH}"
cd $DOCKERFILE_PATH

docker build \
  -t "${DOCKERHUB_REPOSITORY}:${TAG}" \
  .

if [ -z "${DOCKERHUB_TOKEN}" ]; then
  # Skip if secrets aren't populated -- they're only visible for actions running in the repo (not on forks)
  echo "Skipping Docker push"
else
  # Login and push
  docker logout
  docker login --username "${DOCKERHUB_USER}" --password "${DOCKERHUB_TOKEN}"
  docker push "${DOCKERHUB_REPOSITORY}:${TAG}"
fi
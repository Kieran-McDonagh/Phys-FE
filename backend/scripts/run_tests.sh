#!/bin/bash
cd docker/
# Define the Docker Compose test file
DOCKER_COMPOSE_FILE=docker-compose-tests.yaml

# Build and run the tests using Docker Compose
docker compose -f $DOCKER_COMPOSE_FILE up --build --abort-on-container-exit

# Capture the exit code of the docker compose command
EXIT_CODE=$?

# Bring down the Docker Compose services
docker compose -f $DOCKER_COMPOSE_FILE down

# Exit with the exit code from the tests
exit $EXIT_CODE

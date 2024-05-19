#!/bin/bash

# Define the Docker Compose file
DOCKER_COMPOSE_FILE=docker-compose-development.yaml

# Build and run the services using Docker Compose
docker-compose -f $DOCKER_COMPOSE_FILE up --build

# Capture the exit code of the docker-compose command
EXIT_CODE=$?

# Bring down the services
docker-compose -f $DOCKER_COMPOSE_FILE down

# Exit with the exit code from the docker-compose command
exit $EXIT_CODE

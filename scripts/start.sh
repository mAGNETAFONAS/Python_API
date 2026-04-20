#!/bin/bash

export COMPOSE_VERSION=$(cat VERSION.md)
image_name=python_api_web

docker compose -f ./compose.yaml up -d --build

docker tag $image_name:$COMPOSE_VERSION $image_name:latest
#!/bin/bash

export COMPOSE_VERSION=$(cat VERSION.md)
image_name=python-api-web

docker compose -f ./compose.yaml up -d --build
docker image rm $image_name:latest
docker tag $image_name:$COMPOSE_VERSION $image_name:latest
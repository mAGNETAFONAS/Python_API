#!/bin/bash

export COMPOSE_VERSION=$(cat VERSION.md)
image_name=$(cat compose.yaml | grep "image:" | cut -f2 -d: | cut -f2 -d " ")

docker compose -f ./compose.yaml up -d --build

docker tag $image_name:$COMPOSE_VERSION $image_name:latest
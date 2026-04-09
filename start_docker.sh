#!/bin/bash

image_name=$1
container_name=$2
host_port=8000
container_port=8000

docker stop $container_name 2>/dev/null
docker rm $container_name 2>/dev/null

docker run --name "$container_name" -it -d \
--mount type=bind,source="$(pwd)"/files/,target=/app/files/,readonly \
-p $host_port:$container_port "$image_name"
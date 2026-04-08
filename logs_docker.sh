#!/bin/bash

container_name=$1

docker container inspect $container_name > /dev/null 2>&1

if [[ $? = 0 ]]; then
  docker logs $container_name
else
  echo "Container does not exist."
fi
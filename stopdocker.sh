#!/bin/bash

container_name=$1

docker container inspect $container_name > /dev/null 2>&1

if [[ $? = 0 ]]; then
  docker stop $container_name
  echo "Container has been stopped."
else
  echo "Container does not exist."
fi
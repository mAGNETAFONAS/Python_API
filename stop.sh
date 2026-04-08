#!/bin/bash

function prompt() {
  clear
  echo "Do you want to: "
  echo "1. Only stop the container"
  echo "2. Stop and remove the container"
  echo "3. Exit"
  read command
}

prompt

while [[ $command -ne 3 ]]; do
  case $command in
    1)
      docker compose stop
      ;;
    2)
      docker compose down
      ;;
  esac
  prompt
done


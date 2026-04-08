#!/bin/bash

function prompt() {

  echo "Do you want to: "
  echo "1. See a snapshot of logs"
  echo "2. Follow logs"
  echo "3. Exit"
  read command
}

prompt

while [[ $command -ne 3 ]]; do
  case $command in
    1)
      docker compose logs
      ;;
    2)
      docker compose logs -f
      ;;
  esac
  prompt
done

#!/bin/bash

help() {
  echo "Usage: $0 [OPTIONS]"
  echo "Options:"
  echo "-h, --help       Display help message"
  echo "-rm, --remove     Stop and remove docker compose containers"
}


  if [ $# -gt 0 ]; then
    case $1 in
      -h | --help)
        help
        exit 0
        ;;
      -rm | --remove)
        docker compose down
        ;;
      *)
        echo "Invalid argument"
        help
        exit 0
        ;;
    esac
  else :
    docker compose stop
  fi


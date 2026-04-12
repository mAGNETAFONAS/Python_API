#!/bin/bash

help() {
  echo "Usage: $0 [OPTIONS] [IMAGE NAME] [CONTAINER NAME] [HOST PORT] [CONTAINER PORT]"
  echo "Options:"
  echo "-h, --help     Display help message"
}

  if [ $# -eq 1 ]; then
    case $1 in
      -h | --help)
        help
        exit 0
        ;;
      *)
        echo "ERROR: invalid number of arguments"
        help
        ;;
    esac
  else :
    if [ $# -eq 4 ]; then
        docker container ls -a | grep -w "$2" > /dev/null 2>&1
        if [[ $? = 0 ]]; then
          echo "Container with this name already exists."
          exit 0
        else
          docker run --name "$2" -it -d \
          --mount type=bind,source="$(pwd)"/files/,target=/app/files/,readonly \
          -p "$3:$4" "$1"
        fi
    elif [ $# -eq 0 ]; then
        echo "ERROR: No argument given"
        help
        exit 0
    elif [ $# -lt 4 ]; then
        echo "ERROR: Not enough arguments"
        help
        exit 0
    else
        echo "ERROR: Too many arguments"
        help
        exit 0
    fi
  fi

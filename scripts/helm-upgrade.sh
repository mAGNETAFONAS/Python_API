#!/bin/bash

help() {
  echo "Usage: $0 [RELEASE NAME] [CHART] [VALUES FILE PATH] [OPTIONS] "
  echo "Options:"
  echo "-h, --help       Display help message"
}


  if [ $# -eq 1 ]; then
    case $1 in
      -h | --help)
        help
        exit 0
        ;;
      *)
        echo "ERROR: Not enough arguments!"
        help
        ;;
    esac
  elif [ $# -eq 2 ]; then
        echo "ERROR: Not enough arguments!"
        help
  elif  [ $# -eq 3 ]; then
          helm list | grep -w "$1" > /dev/null 2>&1
          if [[ $? = 0 ]]; then
            helm upgrade "$1" "$2" \
              --wait \
              --atomic \
              --timeout 10m \
              -f $3
          else
            echo "ERROR: chart does not exist."
            help
        fi
  elif [ $# -eq 4 ]; then
    help
  elif [ $# -eq 0 ]; then
    echo "ERROR: No argument given"
    help
    exit 0
  elif [ $# -gt 3 ]; then
    echo "ERROR: Too many arguments"
    help
    exit 0


  fi

#!/bin/bash

help() {
  echo "Usage: $0 [OPTIONS] [IMAGE NAME] [VERSION]"
  echo "Options:"
  echo "-h, --help     Display help message"
}


  if [ $# -gt 0 ]; then
    case $1 in
      -h | --help)
        help
        exit 0
        ;;
      *)
        if [ $# -eq 2 ]; then
          echo "Image is being built..."
          docker build -t "$1:$2" .
        else :
          echo "Number of arguments is wrong"
          help
          exit 0
        fi
        ;;
    esac
  else :
    echo "Image name and version not specified"
    help
    exit 0
  fi




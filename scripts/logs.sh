#!/bin/bash

help() {
  echo "Usage: $0 [OPTIONS]"
  echo "Options:"
  echo "-h, --help       Display help message"
  echo "-f, --follow     Follow log output"
}


  if [ $# -gt 0 ]; then
    case $1 in
      -h | --help)
        help
        exit 0
        ;;
      -f | --follow)
        docker compose logs -f
        ;;
      *)
        echo "Invalid argument"
        help
        exit 0
        ;;
    esac
  else :
    docker compose logs
  fi

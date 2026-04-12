#!/bin/bash

help() {
  echo "Usage: $0 [OPTIONS] [CONTAINER NAME]"
  echo "Options:"
  echo "-h, --help       Display help message"
  echo "-f, --follow     Follow log output"
}


  if [ $# -eq 1 ]; then
    case $1 in
      -h | --help)
        help
        exit 0
        ;;
      *)
        docker container ls -a | grep -w $1 > /dev/null 2>&1
        if [[ $? = 0 ]]; then
          docker logs $1
        else
          echo "ERROR: Container does not exist."
          help
        fi
        ;;
    esac
  else :
    if [ $# -eq 2 ]; then
      case $1 in
        -f | --follow)
          docker container ls -a | grep -w $2 > /dev/null 2>&1
          if [[ $? = 0 ]]; then
          docker logs -f $2
        else
          echo "ERROR: Container does not exist."
          help
        fi
        ;;
      esac
    else
      if [ $# -eq 0 ]; then
        echo "ERROR: No argument given"
        help
        exit 0
      elif [ $# -gt 2 ]; then
        echo "ERROR: Too many arguments"
        help
        exit 0
      fi
    fi
  fi

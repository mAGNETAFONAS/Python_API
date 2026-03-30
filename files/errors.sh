#!/usr/bin/bash

if [[ $# -eq 1 ]]; then
    echo "Hello, $1"
else
    echo "Invalid argument"
    exit 1
fi

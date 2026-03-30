#!/usr/bin/bash

conv=({0..1}{0..1}{0..1}{0..1}{0..1})

if [[ $1 -gt 1 && $1 -lt 32 ]]; then
    bin=${conv[$1]}
else
    echo "number out of range"
    exit 1
fi

echo ${bin[@]}
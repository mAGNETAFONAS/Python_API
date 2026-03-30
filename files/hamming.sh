#!/usr/bin/bash

dna1=$1
dna2=$2

if [[ ${#dna1} != ${#dna2} ]]; then
    echo "sequences not same length"
    exit 1
fi
sum=0
for ((i=0; i<${#dna1}; i++)); do
    if [[ "${dna1:$i:1}" == "${dna2:$i:1}" ]]; then
        echo "${dna1:$i:1} and ${dna2:$i:1}"
        continue
    else
        ((sum+=1))
    fi

done

echo "number of mistakes is : $sum"


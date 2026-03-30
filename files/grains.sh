#!/usr/bin/bash

grain_sum=0
square_val=1

for ((i=1 ; i<=64 ; i++)); do
    grain_sum+=$(echo "$grain_sum + $square_val" | bc)
    echo "square $i value is ${square_val#-}"
    square_val=$(echo "$square_val * 2" | bc)
done

echo "Total grain sum is $grain_sum"

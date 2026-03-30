#!/usr/bin/bash

read -p "how many natural numbers?" nat

lst=($(seq 0 1 $nat))
echo "${lst[@]}"

sum1=0
for i in "${lst[@]}"; do

    ((sum1+=$i))
    echo $sum1
done

sum_sqrd=$(($sum1**2))
echo $sum_sqrd

sum2=0
for i in "${lst[@]}"; do

    ((sum2+=$i**2))
    echo $sum2
done

dif=$((sum_sqrd - sum2))
echo $dif
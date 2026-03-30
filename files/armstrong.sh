#!/usr/bin/bash

read -p "enter a number: " num
sum=0

for (( i=0; i<${#num}; i++ )); do
    echo $sum
    n=${num:$i:1}
    ((sum+=$(($n**${#num}))))
    
done

if [[ "$sum" == "$num" ]]; then 
    echo "number is armstrong"
else
    echo "Number is not armstrong"
fi
#!/usr/bin/bash

seq=$1
span=$2

if [[ ${#seq} < $span ]]; then 
    echo "Sequence has less number than span"
    exit 1
elif [[ $seq =~ [^0-9]+ ]]; then 
    echo "sequence must only habe numbers"
    exit 1
elif (( span < 0  )); then 
    echo "span  ust be positive"
    exit 1
fi

max=0
sum=1
for ((i=0; i<=${#seq}-span; i++)); do
echo $i
    sum=1
    for ((a=$i; a<$span+$i; a++)); do   
        num=${seq:$a:1}
        sum=$(( sum * num ))
        
    done
    echo $sum
    
    if [[ $sum -gt $max ]]; then
        max=$sum
    fi
    echo $max

done

echo "largest: $max"
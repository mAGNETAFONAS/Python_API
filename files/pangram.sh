#!/usr/bin/bash

read -p "Typa a pangram: " pan


abc=(a b c d e f g h i j k l m n o p q r s t u v w x y z)

for i in ${abc[@]}; do
    if [[ $pan == *"$i"* ]]; then
        echo $i
        
    else
        echo "Not a pangram"
        exit 1
    fi
done

echo "its a pangram"
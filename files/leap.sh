#!/usr/bin/bash

if [ $(($1%4)) -eq 0 ]; then
    
    if [ $(($1%100)) -eq 0 ]; then
        if [ $(($1%400)) -eq 0 ]; then
            echo "Leap year"
        else
            echo "Not leap year"
        fi
    else
        echo "LEap year"
    fi
else
        echo "Not leap year"

fi
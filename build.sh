#!/bin/bash

image_name=$1
ver=$2

echo "Image is being built..."
docker build -t $image_name:$ver .

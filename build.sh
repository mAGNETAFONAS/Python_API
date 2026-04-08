#!/bin/bash

image_name="python-api"

echo "Image is being built..."
docker build -t $image_name .

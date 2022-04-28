#!/bin/bash

docker run -p 5000:5000 -d payload0911/conv-neural-server:v1
docker run -p 80:80 -d payload0911/conv-neural-client:v1



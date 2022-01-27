#!/bin/bash

for i in {21..30};do
    wget -O images_from_sensor/image"$i".png 'http://192.168.100.104/capture?_cb=arturo.png'
    sleep 2
done

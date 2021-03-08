#!/bin/sh


#docker build -t base_image $1 &

docker-compose run  -v mongodata:/data/db -d -p 27017:27017 mongodb

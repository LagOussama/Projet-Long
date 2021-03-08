
#!/bin/sh

cd $1 &

#docker image rm -f  snifferenv &

#docker build -t base_image $1 &

docker-compose run -p 5000:5000 websniff

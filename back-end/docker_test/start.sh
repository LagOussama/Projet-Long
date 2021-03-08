#!/bin/sh
#<docker files directery>  <nber of Cl1>  <nber of Cl2>

cd $1 &



#docker image rm -f  client &
#docker image rm -f  client2 &



for (( i = 1; i <= $2; i++ )) 
do 
        docker-compose run  client1 &
done


for (( i = 1; i <= $3; i++ )) 
do 
       docker-compose run  client2 &
done

echo "installation suscessfull"

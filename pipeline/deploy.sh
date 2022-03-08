#!/bin/bash
#create docker network
docker network create mynetwork
# build flask app and mysql
docker build -t databasemysql:8 database
docker build -t flask-library:latest .

#run mysql container
docker run -d --name mysql --network mynetwork databasemysql:8

#run flask container
docker run -d --name flask-app --network mynetwork flask-library:latest 

#run nginx container
docker run -d --name nginx -p 80:80 --network mynetwork --mount type=bind,source=$(pwd)/nginx.conf,target=/etc/nginx/nginx.conf nginx:latest

show running containers


docker ps

#!usr/bin/env sh
# get the latest updates
git pull origin master
# force current containers to stop
docker-compose down
# build and run the containers in a detatched state
docker-compose up --build -d
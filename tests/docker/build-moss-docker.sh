#! /bin/bash

# Build
docker build -t moss/moss-test-image:latest .
docker create -it --name moss moss/moss-test-image:latest
docker start moss

# Set root password for SSH
echo "--------------------- [ Set moss container root password ] ---------------------"
docker exec -it moss passwd
docker exec -it moss /etc/moss/run-services.sh

#! /bin/bash

docker_image_present=$(docker images | grep moss/moss-test-image)

if [[ ! -n "$docker_image_present"  ]]; then
  echo "Building moss Docker image"
  sleep 2

  cd ../docker/
  docker build -t moss/moss-test-image:latest .
  docker create -it --name moss --privileged --cap-add=ALL -p 22:22 moss/moss-test-image:latest
fi

docker_start_result=$(docker start moss)

echo "--------------------- [ Set moss container root password ] ---------------------"
docker exec -it moss passwd

if [[ $docker_start_result == *"Error response from daemon:"* ]]; then
  echo "Unable to start moss container."
fi

docker exec -it moss /etc/moss/run-services.sh

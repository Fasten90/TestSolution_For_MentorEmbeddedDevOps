docker stop myapp_container
docker rm myapp_container

docker build . --tag myapp

docker run -d \
    --name myapp_container \
    myapp


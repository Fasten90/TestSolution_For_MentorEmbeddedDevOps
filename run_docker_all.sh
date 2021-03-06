docker rm myapp_container
docker rm mysql-test
docker rm rest-api-test

docker build . --tag myapp

docker network create isolated-network

docker run -d \
    -e MYSQL_ROOT_PASSWORD=secret \
    -p 3306:3306 \
    --name mysql-test \
    --network=isolated-network \
    mentorembeddeddevops/mysql-test:1.0

docker run -d \
    --name rest-api-test \
    -p 80:5000 \
    --network=isolated-network \
    mentorembeddeddevops/rest-api-test:1.0

sleep 20

docker run -d \
    --name myapp_container \
    --network=isolated-network \
    myapp


docker stop myapp_container
docker stop mysql-test
docker stop rest-api-test
#docker rm myapp_container
#docker rm mysql-test
#docker rm rest-api-test

docker network rm isolated-network


docker stop mysql-test
docker rm mysql-test
docker pull mentorembeddeddevops/mysql-test:1.0

docker run -d \
    -e MYSQL_ROOT_PASSWORD=secret \
    -p 3306:3306 \
    --name mysql-test \
    mentorembeddeddevops/mysql-test:1.0


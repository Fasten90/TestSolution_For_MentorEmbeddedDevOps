docker stop rest-api-test
docker rm rest-api-test
docker pull mentorembeddeddevops/rest-api-test:1.0

docker run -d \
    --name rest-api-test \
    -p 80:5000 \
    mentorembeddeddevops/rest-api-test:1.0



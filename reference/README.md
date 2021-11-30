# mentorembeddeddevops

Repository for the source additional files and other stuff

## Tasks

1. Download and run these docker images:
	- [`mentorembeddeddevops/mysql-test:1.0`](https://hub.docker.com/r/mentorembeddeddevops/mysql-test) to act as the database for the rest of the tasks
	- [`mentorembeddeddevops/rest-api-test:1.0`](https://hub.docker.com/r/mentorembeddeddevops/rest-api-test) which hosts a simple http server for the rest of the tasks
2. Write a python 3 script that does the following:
	- Queries the mysql database for employees working in the `Production` deparment, earning more than `100` (see [db schema](https://hub.docker.com/r/mentorembeddeddevops/mysql-test)). Recommended to use the `mysql-connector-python` package.
	- Some of these employees are users of the site hosted by the container `rest-api-test`, with various access levels. Use the site's REST API to get the username of those among them who have `WRITE` access. See API documentation on the main page of the site. (note: some of the employees might not be users here at all)
	- Write the results of the queries in a CSV file which has three columns:
		- `Name` (All returned by the mysql query)
		- `Birthday`
		- `Username` (`N/A` if not a user of the site or doesn't have `WRITE` access)
	- See [example output](https://github.com/Vafthrudnir/mentorembeddeddevops/blob/4b853ea82d773a00b59b90dbfece1c92a2a80108/output.csv) (note: csv dialect is not important now, feel free to leave it on defaults)
3. Create a Dockerfile based on image [`python:3.10.0-bullseye`](https://hub.docker.com/_/python) that runs the script you wrote.
4. Write a shell script that:
	- Creates the docker network,
	- builds your docker image based on the Dockerfile created previously,
	- runs all three containers, connecting them to the same network (note: some time will be needed for the mysql-test container to start up, the python container will not be able to communicate with it during this time),
	- stops the mysql-test and the tool-inventory-test containers once the python container finished running,
	- deletes all containers (if not deleted automatically)
5. Upload your work to a github repository

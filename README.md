# containerize-python-flask-application-using-docker
Deploy a simple webserver application using the Flask library in Python. Then containerize the application using Docker, with the use of Dockerfile and docker-compose.yml

## How it works
In our 'Dockerfile' file, we give instructions on how to build the Docker image. For this example, we are simply using a python image, version 3.11.0. We are also creating a directory in the image called 'python-flask', which we set as the working directory. This will all our files into the directory. Finally, we direct the image to install all necessary dependencies (Flask) to run the application, from the 'requirements.txt' file.

Next, the 'docker-compose.yml' file describes how to run the Docker container based off the Docker image created. We are making sure we are running Python version 3.11 and that we are building the parent folder. Then, we are binding the Docker container's 5000 port to the host machine's 8080 port. 

This makes it so we can access the web application on a different port than the one used by the Docker container, allowing us to run multiple Flask applications in seperate containers with their default ports, but still be able to assign different local ports in order to avoid conflicts.

Lastly, we specify the volume of the application. We do this rather than binding a mount point, to remove the dependency of the host machine, given that volumes are completely mananged by Docker. 

## How to run
To run the Flask application, simply run the `docker compose up` command in the app directory. This will create the docker container and run it at the same time.

You will then be able to access the web application using your browser, going to `http://localhost:8080` or using the CLI with the command `curl http://localhost:8080`.
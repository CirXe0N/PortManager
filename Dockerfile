FROM python:latest
MAINTAINER CIRX Software, cirxsoftware@gmail.com

## Copy file to docker image
ADD requirements.txt /app/requirements.txt

# Change to the directory of the project
WORKDIR /app/

# Install project dependencies
RUN pip install -r requirements.txt

# Start from a lightweight Python Alpine base image
FROM python:3.9.18-alpine3.18

# Update package list and install Flask directly
# The --no-cache option avoids the need to use apk cache and reduces the size of the container
RUN apk update && apk add --no-cache && pip install Flask

# Set the working directory in the container to /app
# All subsequent commands will be run from this directory
WORKDIR /app

# Copy the contents of the local app directory to the /app directory in the container
# This includes all of your Flask application files, like api.py
COPY ./app .

# Define the command to run your Flask application
# CMD is executed when the Docker container starts up
CMD ["python3", "api.py"]

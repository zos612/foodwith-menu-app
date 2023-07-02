# Use the official Python 3 image as the base
FROM python:3.9

# Set up the working directory inside the container
WORKDIR /app

# Copy the code from the local machine to the container
COPY . /app

# Install any required dependencies
RUN apt-get update -y && \
	apt-get install -y cron \
	pip install requests \
	
	

# Specify the command to run when the container starts
CMD service cron start
CMD systemctl enable cron.service
CMD [ "python", "selenium01.py" ]

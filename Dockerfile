# Use the official Python 3 image as the base
FROM python:3.9

# Set up the working directory inside the container
WORKDIR /home/app

# Copy the code from the local machine to the container
COPY . /home/app/temp
# COPY ./google-chrome-stable_current_amd64.deb /app/google-chrome-stable_current_amd64.deb

# RUN chmod 0644 /app/app.py

# Install any required dependencies
RUN apt-get -y update 
RUN apt-get -y install sudo wget unzip vim
RUN apt-get -y install cron
RUN apt-get -y install ./temp/google-chrome-stable_current_amd64.deb


# RUN apt-get install -y xvfb
RUN pip install requests
RUN pip install beautifulsoup4 
RUN pip install selenium
RUN pip install schedule

#linux 용 chrome 설치 
# RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# RUN wget -O google-chrome-stable_current_amd64.deb https://www.slimjet.com/chrome/download-chrome.php?file=files%2F104.0.5112.102%2Fgoogle-chrome-stable_current_amd64.deb
# RUN apt-get -y install ./google-chrome-stable_current_amd64.deb
RUN mv /usr/bin/google-chrome-stable /usr/bin/google-chrome

#chromedriver 설치
# RUN wget https://chromedriver.storage.googleapis.com/104.0.5112.79/chromedriver_linux64.zip
# RUN unzip chromedriver_linux64.zip
RUN mv ./temp/chromedriver /usr/bin/chromedriver


RUN rm -r /home/app/temp

# CMD python /app/app.py > output.log 2>&1

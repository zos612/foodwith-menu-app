@echo off

docker stop food-with-menu-app
docker rm food-with-menu-app
docker rmi food-with-menu-app
docker build -t food-with-menu-app .

docker run -it --name food-with-menu-app food-with-menu-app bash

timeout /t 1
python app.py
@echo off

docker stop food-with-menu-app
docker rm food-with-menu-app
docker rmi food-with-menu-app
docker build -t food-with-menu-app .

docker run -it -v .:/home/app --name food-with-menu-app food-with-menu-app bash
@REM nohup python -u app.py >> app.log 2>&1 &
@REM nohup python -u token_refresher.py >> token_refresher.log 2>&1 &
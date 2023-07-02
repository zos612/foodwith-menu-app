import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from datetime import datetime
import urllib.request
import os.path
from os import path

basic_url = "https://pf.kakao.com"

foodWithUrl = basic_url + "/_eAGqxb"

driver = webdriver.Chrome()
driver.get(foodWithUrl)

sleep(0.5)

foodWithHTML = driver.page_source

# print(html)

soup = BeautifulSoup(foodWithHTML, "html.parser")

# 푸드위드 첫 번째 게시글 a태그
# a_item = soup.select_one(".list_news > li:nth-child(1) > a")
# sub_url = a_item['href']

sub_url = soup.select_one(".list_news > li:nth-child(1) > a")['href']

# print("item :", a_item)

# print("item.href. :", a_item['href'])

second_url = basic_url + sub_url

print("second_url :", second_url)

driver.get(second_url)

sleep(0.5)

secondHTML = driver.page_source
soup = BeautifulSoup(secondHTML, "html.parser")

#이미지 url 가져오기
imgUrl = 'https:' + soup.select_one(".post_card > .card_default.card_image > .wrap_thumb > div > img")['src']

#포스팅일 가져오기
postTime = soup.select_one('.post_profile > .wrap_info > .txt_time > a').text


currentYear = datetime.today().strftime("%Y")

postTimeSplit = postTime.split()

postDate_kr = currentYear + '년 ' + postTimeSplit[0] + ' ' + postTimeSplit[1]
print("포스팅일: ", postDate_kr)

datetime_format = "%Y년 %m월 %d일"
postDate_YYMMDD = datetime.strptime(postDate_kr, datetime_format).strftime("%Y%m%d")

#현재 날짜
currentDate_YYMMDD = datetime.today().strftime("%Y%m%d")

#포스팅 날짜와 현재 날짜가 같지 않으면 실행 종료
if postDate_YYMMDD != currentDate_YYMMDD :
    print("포스팅 날짜와 현재 날짜가 같지 않습니다.")
    exit()

#이미지 저장 경로
image_path = './images/' + currentDate_YYMMDD +'.jpg'

#이미지가 존재하면 저장x
if path.exists(image_path) == False :
    print("이미지가 이미 존재합니다.")
    urllib.request.urlretrieve(imgUrl, image_path)



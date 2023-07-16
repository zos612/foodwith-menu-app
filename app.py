import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
import urllib.request
import os.path
from os import path
import requests
import json
import schedule
import time

#카카오톡 메세지 보내기
def send_message(image_path, menu_url):
  with open('kakao_code.json', 'r') as f:
      kakao_code = json.load(f)

  access_token = kakao_code['access_token']

  url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
  headers = {
      "Authorization": "Bearer " + access_token
  }
  data = {
      "template_object" : 
      json.dumps({
            "object_type": "feed",
            "content": {
              "title": '오늘의 메뉴',
              "description": "#푸드위드",
              "image_url":
                image_path,
              "link": {
                "mobile_web_url": menu_url,
                "web_url": menu_url
              }
            }
          })
  }

  response = requests.post(url, headers=headers, data=data)
  if response.json().get('result_code') == 0:
      print('메시지를 성공적으로 보냈습니다.')
  else:
      print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))

#메인 함수
def main():

  print('작업 실행시간:', datetime.now())

  basic_url = "https://pf.kakao.com"

  foodWithUrl = basic_url + "/_eAGqxb"

  # Set the path to the chromedriver executable
  chromedriver_path = '/usr/bin/chromedriver'

  # Configure Chrome options
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument('--headless')  # Run Chrome in headless mode (without GUI)

  # linux 환경에서 필요한 option
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')

  # Create the WebDriver
  driver = webdriver.Chrome(options=chrome_options)

  driver.get(foodWithUrl)

  sleep(0.5)

  foodWithHTML = driver.page_source

  soup = BeautifulSoup(foodWithHTML, "html.parser")

  sub_url = soup.select_one(".list_news > li:nth-child(1) > a")['href']

  second_url = basic_url + sub_url

  # print("second_url :", second_url)

  driver.get(second_url)

  sleep(0.5)

  secondHTML = driver.page_source
  soup = BeautifulSoup(secondHTML, "html.parser")

  #이미지 url 가져오기
  imgUrl = 'https:' + soup.select_one(".post_card > .card_default.card_image > .wrap_thumb > div > img")['src']

  #포스팅일 가져오기
  postTime = soup.select_one('.post_profile > .wrap_info > .txt_time > a').text

  #현재 날짜
  currentDate_YYMMDD = datetime.today().strftime("%Y%m%d")
  # currentDate_YYMMDD = datetime(2023,7,14).strftime("%Y%m%d")

  currentYear = datetime.today().strftime("%Y")

  postTimeSplit = postTime.split()

  # 포스팅 시간이 '년'으로 시작하는 경우
  if '월' in postTimeSplit[0] :
      postDate_kr = currentYear + '년 ' + postTimeSplit[0] + ' ' + postTimeSplit[1]
      # print("포스팅일:", postDate_kr)

      datetime_format = "%Y년 %m월 %d일"
      postDate_YYMMDD = datetime.strptime(postDate_kr, datetime_format).strftime("%Y%m%d")

      #포스팅 날짜와 현재 날짜가 같지 않으면 실행 종료
      if postDate_YYMMDD != currentDate_YYMMDD :
          print("신규 포스팅 없음")
          return

  #이미지 저장 경로
  image_path = './images/' + currentDate_YYMMDD +'.jpg'

  #이미지가 존재하면 저장x
  if path.exists(image_path) == True :
      print("이미 보낸 메뉴입니다.")
      return

  #이미지 저장
  urllib.request.urlretrieve(imgUrl, image_path)
  print(datetime.today().strftime("%Y-%m-%d") + '일자 이미지 다운로드 완료.')

  driver.quit()

  send_message(imgUrl, second_url)


main()

schedule.every().hour.do(main)

while True:
  # print('schedule.run_pending()')
  schedule.run_pending()
  time.sleep(1)
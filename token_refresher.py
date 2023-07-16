# 라이브러리 호출
import requests
import json
import schedule
import time
from datetime import datetime

def job():
    print('작업 실행시간:', datetime.now())
    # 카카오톡 메시지 API
    url = "https://kauth.kakao.com/oauth/token"
    data = {
        "grant_type" : "refresh_token",
        "client_id" : "0df3b630c4634ebd737f58c96b5e74be",
        "refresh_token": "wslaYqGO8X9Dd0XFx2KBr4RSQmfxomrxiCzZjXdrCinJXwAAAYlYjzfM"
    }
    response = requests.post(url, data=data)
    tokens = response.json()
    print(tokens)

    # kakao_code.json 파일 저장
    with open("kakao_code.json", "w") as fp:
        json.dump(tokens, fp)
        print("액세스 토큰이 생성되었습니다.")

# job()

schedule.every(6).hours.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
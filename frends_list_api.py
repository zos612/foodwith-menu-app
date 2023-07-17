# 라이브러리 호출
import requests
import json

# 카카오 API 엑세스 토큰
with open("kakao_code.json", "r") as fp:
    tokens = json.load(fp)    


url = "https://kapi.kakao.com/v1/api/talk/friends" #친구 목록 가져오기

header = {"Authorization": 'Bearer ' + tokens["access_token"]}

result = json.loads(requests.get(url, headers=header).text)
print(result)

friends_list = result.get("elements")
print(friends_list)

# 라이브러리 호출
import requests
import json

# 카카오톡 메시지 API
url = "https://kauth.kakao.com/oauth/token"
data = {
    "grant_type" : "authorization_code",
    "client_id" : "0df3b630c4634ebd737f58c96b5e74be",
    "redirect_url" : "https://localhost:3000",
    "code" : "z67SZgxow8VpY_t_47tKLhJBHbP4CC8Q9Tj0UbwmrW374uHiT3bEmEq9pB08ADK0w2wmYAopyWAAAAGJZEVCww"
}
response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# kakao_code.json 파일 저장
with open("kakao_code.json", "w") as fp:
    json.dump(tokens, fp)
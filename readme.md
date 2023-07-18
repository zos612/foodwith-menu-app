# 소개
푸드위드 사이트에 메뉴를 크롤링해서 카카오 메세지를 보내는 앱입니다.   

**푸드위드 사이트**   
https://pf.kakao.com/_eAGqxb    
# 실행 방법
### 앱실행
nohup python -u app.py >> app.log 2>&1 &   
### 토큰 갱신
nohup python -u token_refresher.py >> token_refresher.log 2>&1 &   
### 참고 사이트
카카오 API를 이용하여 나에게 메시지 보내기   
https://foss4g.tistory.com/1624 

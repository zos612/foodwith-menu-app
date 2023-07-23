# 소개
푸드위드 사이트의 메뉴를 크롤링해서 카카오 메세지를 보내는 앱입니다.  

![image](https://github.com/zos612/food-with-menu-app/assets/13166673/8aa070d6-eb2f-49ba-bf13-7c544a9066b9)

**푸드위드 사이트**   
https://pf.kakao.com/_eAGqxb    
# 실행 방법
### 인가코드 받기
1. 아래 주소를 브라우저 주소창에 입력하고 카카오톡 로그인을 한 후 카카오톡 권한을 수락한다.   
https://kauth.kakao.com/oauth/authorize?client_id=0df3b630c4634ebd737f58c96b5e74be&redirect_uri=https://localhost:3000&response_type=code&scope=talk_message   

2. https://localhost:3000 주소로 이동하며 주소 창에 code={인가코드}를 복사한다.   

3. token_creator.py 코드에 code부분에 인가코드를 넣고 실행한다.

4. kakao_code.json에 엑세스 토큰과 리프레쉬 토큰이 새로 생성된다.

### 도커 빌드 및 실행
docker build -t food-with-menu-app .   
docker run -it -v .:/home/app --name food-with-menu-app food-with-menu-app bash
### 앱실행
nohup python -u app.py >> app.log 2>&1 &   
### 토큰 갱신
nohup python -u token_refresher.py >> token_refresher.log 2>&1 &   
### 참고 사이트
카카오 API를 이용하여 나에게 메시지 보내기   
https://foss4g.tistory.com/1624 

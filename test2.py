import requests

# API 엔드포인트 URL
url = 'https://naver.com'

# GET 요청 보내기
response = requests.get(url)

# 응답 상태코드 확인
if response.status_code == 200:
    # JSON 데이터 추출


    # 데이터 출력
    print('성공', type(response))
else:
    print("에러 발생. 상태코드:", response.status_code)

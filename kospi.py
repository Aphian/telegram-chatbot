import requests
from bs4 import BeautifulSoup

# URL 요청 => Doc 응답 => Data 추출 
URL = 'https://finance.naver.com/sise/'
# URL 로 요청을 보내고, 응답을 받는다.
res = requests.get(URL)
# 응답을 받은 HTML 문서를 구문 분석
soup = BeautifulSoup(res.text, 'html.parser')
# 구문 분석된 결과에서, 원하는 데이터를 선택
kospi = soup.select_one('#KOSPI_now')
kosdaq = soup.select_one('#KOSDAQ_now')
kospi200 = soup.select_one('#KPI200_now')

print('kospi : ' + kospi.text)
print('kosdaq : ' + kosdaq.text)
print('kospi200 : ' + kospi200.text)

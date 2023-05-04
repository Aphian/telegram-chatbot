# import
import requests
from bs4 import BeautifulSoup

# URL 과 TOKEN 세팅
TOKEN = '6178945223:AAFZMM3tqF_EDQvUiJc1Rvu2GhTbUz4YMwY'
BASE_URL = f'https://api.telegram.org/bot{TOKEN}'

# getUudate 로 메시지 받아오기 
response = requests.get(BASE_URL + '/getUpdates').json()

# 마지막 메시지의 발신자/내용 가져오기
last_chat_id = response['result'][-1]['message']['chat']['id']
last_msg = response['result'][-1]['message']['text']

# 마지막 메시지의 내용을 판단하여, 최종적으로 답장할 메시지 생성
if last_msg == '주식':
    URL = 'https://finance.naver.com/sise/'
    res = requests.get(URL)
    soup = BeautifulSoup(res.text, 'html.parser')

    kospi = soup.select_one('#KOSPI_now')
    kosdaq = soup.select_one('#KOSDAQ_now')
    kospi200 = soup.select_one('#KPI200_now')
    return_msg = f'KOSPI: {kospi.text}, KOSDAQ : {kosdaq.text}, KOSQI200 : {kospi200.text}'

elif last_msg in ['로또', 'lotto', 'Lotto']:
    URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1065'
    res = requests.get(URL)
    data = res.json()
    numbers = []

    for i in range(1, 7):
        numbers.append(data[f'drwtNo{i}'])
    return_msg = f"번호 : {numbers}, 보너스 : {data['bnusNo']}, 상금 : {data['firstWinamnt']}"
    ## print('1, 2, 3, 4, 5, 6, 7, 1000000')
    
elif last_msg.split()[0] == '쇼핑' :
    URL = f'https://openapi.naver.com/v1/search/shop.json?query={last_msg.split()[1]}'
    headers = {    
        'X-Naver-Client-Id' : 'SSO3GRfmtsics4OrPq92',
        'X-Naver-Client-Secret' : 'XKC8TVhwpT'
    }
    res = requests.get(URL, headers=headers).json()
    return_msg = res['items'][0]
    ## print('최저가 검색: ')
    ## print(last_msg.split()[1])
else:
    return_msg = '모르는 명령어 입니다.'

# 마지막 메시지의 발신자에게 답장할 메시지를 보냄
requests.get(BASE_URL + f'/sendMessage?chat_id={last_chat_id}&text={return_msg}')

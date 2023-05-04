# import
import requests
from bs4 import BeautifulSoup
import utils


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
    return_msg = utils.get_kospi()

elif last_msg in ['로또', 'lotto', 'Lotto']:
    return_msg = utils.get_lotto()

elif last_msg.split()[0] == '쇼핑' :
    item = last_msg.split()[1]
    return_msg = utils.get_naver_shopping(item)

else:
    return_msg = '모르는 명령어 입니다.'

# 마지막 메시지의 발신자에게 답장할 메시지를 보냄
requests.get(BASE_URL + f'/sendMessage?chat_id={last_chat_id}&text={return_msg}')

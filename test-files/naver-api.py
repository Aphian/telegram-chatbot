import requests

from dotenv import load_dotenv
import os

load_dotenv()

NAVER_CLEINT_ID = os.environ['NAVER_Client_ID']
NAVER_CLEINT_SCRET_ID = os.environ['NAVER_Client_Secret']

def get_naver_shopping(item):

    URL = f'https://openapi.naver.com/v1/search/shop.json?query={item}'
    headers = {    
        'X-Naver-Client-Id' : NAVER_CLEINT_ID,
        'X-Naver-Client-Secret' : NAVER_CLEINT_SCRET_ID
    }

    res = requests.get(URL, headers=headers).json()
    result = res['items'][0]
    msg = f"{result['title']} : {result['lprice']}원 \n {result['link']}"
    return msg

# print(get_naver_shopping('오렌지'))
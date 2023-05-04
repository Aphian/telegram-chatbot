import requests

URL = 'https://openapi.naver.com/v1/search/shop.json?query=GTX3060'
headers = {    
    'X-Naver-Client-Id' : 'SSO3GRfmtsics4OrPq92',
    'X-Naver-Client-Secret' : 'XKC8TVhwpT'
}

res = requests.get(URL, headers=headers)

print(res.json()['items'][0])
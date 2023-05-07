from flask import Flask, request
import requests
from dotenv import load_dotenv
import os

import utils

load_dotenv()

app = Flask('telegram-chatbot')

TOKEN = os.environ['BOT_TOKEN']
BASE_URL = f'https://api.telegram.org/bot{TOKEN}'

@app.route('/telegram', methods=['POST']) 
def telegram():
    data = request.json
    print('TELEGRAM에서 요청이 들어왔다!')
    chat_id = data['message']['from']['id']
    message = data['message']['text']
    # print(chat_id, message)

    # Response
    # if message == '주식':
    #     return_msg = utils.get_kospi()

    # if message in ['로또', 'lotto', 'Lotto']:
    #     return_msg = utils.get_lotto()

    # elif message.split()[0] == '쇼핑' :
    #     item = message.split()[1]
    #     return_msg = utils.get_naver_shopping(item)

    # else:
    #     return_msg = '모르는 명령어 입니다.'
    return_msg = '모르는 명령어 입니다.'
    requests.get(BASE_URL + f'/sendMessage?chat_id={chat_id}&text={return_msg}')

    return 'Telegram CHATBOT'

# ~~~ '/hello'이렇게 요청이 들어오면, 아래 함수를 실행해라.
@app.route('/hello')
def hello():
    # 'Hello World!!!' 라도 응답 해라.
    return 'Hello World!'

if __name__ == '__main__':
    app.run(port=80, debug=True)
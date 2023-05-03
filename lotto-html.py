import requests
from bs4 import BeautifulSoup

URL = 'https://search.naver.com/search.naver?query=%EB%A1%9C%EB%98%90'

res = requests.get(URL)

soup = BeautifulSoup(res.text, 'html.parser')

no1 = soup.select_one('#main_pack > div.sc_new.cs_lotto._lotto > div > div.content_area > div > div > div:nth-child(2) > div.win_number_box > div > div.winning_number > span.ball.type1')
no2 = soup.select_one('#main_pack > div.sc_new.cs_lotto._lotto > div > div.content_area > div > div > div:nth-child(2) > div.win_number_box > div > div.winning_number > span:nth-child(2)')
no3 = soup.select_one('#main_pack > div.sc_new.cs_lotto._lotto > div > div.content_area > div > div > div:nth-child(2) > div.win_number_box > div > div.winning_number > span:nth-child(3)')
no4 = soup.select_one('#main_pack > div.sc_new.cs_lotto._lotto > div > div.content_area > div > div > div:nth-child(2) > div.win_number_box > div > div.winning_number > span.ball.type3')
no5 = soup.select_one('#main_pack > div.sc_new.cs_lotto._lotto > div > div.content_area > div > div > div:nth-child(2) > div.win_number_box > div > div.winning_number > span.ball.type4')
no6 = soup.select_one('#main_pack > div.sc_new.cs_lotto._lotto > div > div.content_area > div > div > div:nth-child(2) > div.win_number_box > div > div.winning_number > span.ball.type5')
bonus_no = soup.select_one('#main_pack > div.sc_new.cs_lotto._lotto > div > div.content_area > div > div > div:nth-child(2) > div.win_number_box > div > div.bonus_number > span')
prize = soup.select_one('#main_pack > div.sc_new.cs_lotto._lotto > div > div.content_area > div > div > div:nth-child(2) > div.win_number_box > p > strong')

print('당첨번호 : ', no1.text, no2.text, no3.text, no4.text, no5.text, no6.text)
print('보너스 번호 : ', bonus_no.text)
print ('당첨금 : ', prize.text,'원')
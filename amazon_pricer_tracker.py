from email import header
import requests
from bs4 import BeautifulSoup
import time
from token import *
# requestsでHTMLを取得し
#  BeautifulSoupでパースする流れ

amazon_url = 'https://www.amazon.co.jp/Python%E3%81%A7%E3%81%AF%E3%81%98%E3%82%81%E3%82%8B%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92-%E2%80%95scikit-learn%E3%81%A7%E5%AD%A6%E3%81%B6%E7%89%B9%E5%BE%B4%E9%87%8F%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%8B%E3%82%A2%E3%83%AA%E3%83%B3%E3%82%B0%E3%81%A8%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92%E3%81%AE%E5%9F%BA%E7%A4%8E-Andreas-C-Muller/dp/4873117984/ref=sr_1_8?keywords=python%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92&qid=1660149428&sprefix=Python%E6%A9%9F%E6%A2%B0%2Caps%2C383&sr=8-8'

def amazon_tracking_price():
    amazon_page = requests.get(amazon_url)
    # html.parser .. html形式でパース
    soup = BeautifulSoup(amazon_page.content, 'html.parser')
    # print(soup)
    title = soup.find(id="productTitle").get_text()
    print("TITLE: {}".format(title))
    price = soup.find('span', class_="header-price").get_text()
    print("PRICE: {}".format(price))
    convert_price = int(price[1:6].replace(",",''))
    print("CONVERT_PRICE: {}".format(convert_price))

    if(convert_price > 3000):
        send_line_notification()

def send_line_notification():
        ACCESSTOKEN = TOKEN
        line_notify_api = "https://notify-api.line.me/api/notify"
        headers = {"authorization":f"Bearer {ACCESSTOKEN}"}
        data = {"message":"Now! {}".format(amazon_url)}
        requests.post(line_notify_api, headers=headers,data=data)

# # 自動呼び出し
# while(True):
#     print('Trakking...')
#     time.sleep(5)
#     amazon_tracking_price()


amazon_tracking_price()
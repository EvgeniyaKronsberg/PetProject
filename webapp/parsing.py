import requests
import time
from bs4 import BeautifulSoup
from datetime import datetime

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False

def check_price(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        price = soup.find('span', class_='ProductHeader__price-default_current-price js--ProductHeader__price-default_current-price').text
        raw_price = soup.find('span', class_='ProductHeader__price-default_current-price js--ProductHeader__price-default_current-price').text
        price = raw_price.replace("\n","").strip()
        return price
    except(AttributeError):
        print('Товара нет в наличии')
        return False



if __name__ == '__main__':
    html = get_html(input('Введите html-ссылку для отслеживания товара на сайте citilink.ru: '))
    if html:
        time.sleep(3)
        price = check_price(html)
        current_date = datetime.now()
        result = [price, current_date]
        print(result)

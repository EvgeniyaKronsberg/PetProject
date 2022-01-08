import requests
import time
from bs4 import BeautifulSoup
from datetime import datetime

from requests.exceptions import Timeout
from requests_html import HTMLSession

def get_html(url):
    try:
        session = HTMLSession()
        result = session.get(url)
        result.raise_for_status()
        # session = HTMLSession()
        # result = session.get(url)        
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False

def get_soup():
    #html = get_html(input('Введите html-ссылку для отслеживания товара на сайте citilink.ru: '))

    html = get_html('https://www.citilink.ru/product/igrovaya-konsol-nintendo-switch-seryi-1183183/?text=nintendo')   #citylink
    return BeautifulSoup(html, 'html.parser')

def check_price(soup):
    try:
        price_block = soup.find('div', class_='ProductHeader__price-block')
    except AttributeError:
        print('Ошибка проверки цены')
    try:
        raw_price = price_block.find('span', class_='ProductHeader__price-default_current-price js--ProductHeader__price-default_current-price').text
        price = float(raw_price.replace('\n','').replace(' ',''))
        return price
    except(AttributeError):
        checker=price_block.find('h2', class_='ProductHeader__not-available-header').text
        if checker == 'Нет в наличии':
            print('Товара нет в наличии')
        return False


if __name__ == '__main__':
    soup = get_soup()    
    if soup:
        time.sleep(3)
        price = check_price(soup)
        search_datetime_raw = datetime.now()
        search_datetime = search_datetime_raw.strftime('%d.%m.%Y %H:%M')
        result = [price, search_datetime]
        print(result)

from flask import current_app
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
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False


def get_search_url():
    search_query = input('Введите название товара для отслеживания на сайте citilink.ru: ').split()
    temp_url = 'https://www.citilink.ru/search/?text='
    for word in search_query:
        print(word)
        temp_url = temp_url + word + '+'
    url = temp_url[:-1]
    return url


def get_soup():
    #html = get_html(input('Введите html-ссылку для отслеживания товара на сайте citilink.ru: '))

    #html = get_html('https://www.citilink.ru/product/igrovaya-konsol-nintendo-switch-seryi-1183183/?text=nintendo')   #citylink

    search_url = get_search_url()
    html = get_html(search_url)
    if html:
        with open("citylink_search_test.html", "w", encoding="utf8") as f:
            f.write(html)

    return BeautifulSoup(html, 'html.parser')


def get_search_results(soup):
    try:
        # found_products = soup.findAll('div')
        
        # found_products_grid = soup.find('div', class_='ProductCardCategoryList__grid')
        found_products_grid = soup.find('section', class_='GroupGrid js--GroupGrid GroupGrid_has-column-gap GroupGrid_has-row-gap')
        
        found_products = found_products_grid.find('div', class_='product_data__gtm-js product_data__pageevents-js  ProductCardVertical js--ProductCardInListing ProductCardVertical_normal ProductCardVertical_shadow-hover ProductCardVertical_separated')
        print(type(found_products))
        print(found_products)
    except AttributeError:
        print('Ошибка поиска')


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
        time.sleep(6)
        get_search_results(soup)
    #     price = check_price(soup)
    #     search_datetime_raw = datetime.now()
    #     search_datetime = search_datetime_raw.strftime('%d.%m.%Y %H:%M')
    #     result = [price, search_datetime]
    #     print(result)
from bs4 import BeautifulSoup
import requests
import time

def web_scraper(url):
    target_page = requests.get(url)
    soup = BeautifulSoup(target_page.text, 'html.parser')

    restaurants = soup.findAll('h2', attrs={'class': 'customer-item-name'})
    addresses = soup.findAll('span', attrs={'class': 'customer-info-detail highlighted address'})


    for restaurant, address in zip(restaurants, addresses):
        print('Restaurant: ' + restaurant.text)
        print('Address: ' + address.text)

base_url = 'https://www.infobel.com/en/uk/business/10000/food_restaurants'
page_number = 1

while True:
    page_url = f'{base_url}/{page_number}'
    web_scraper(page_url)

    page_number += 1

    if page_number > 3:
        break
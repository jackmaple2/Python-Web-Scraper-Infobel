from bs4 import BeautifulSoup
import requests

target_page = requests.get('https://www.infobel.com/en/uk/business/10000/food_restaurants')

soup = BeautifulSoup(target_page.text, 'html.parser')

restaurants = soup.findAll('h2', attrs={'class': 'customer-item-name'})
addresses = soup.findAll('span', attrs={'class': 'customer-info-detail highlighted address'})


for restaurant, address in zip(restaurants, addresses):
    print('Restaurant: ' + restaurant.text)
    print('Address: ' + address.text)
    



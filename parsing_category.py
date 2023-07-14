from bs4 import BeautifulSoup
import requests

url = "https://stroydvor.kg/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
categories = soup.find_all('div', class_='dark_link')
# print(categories)
for category in categories:
    print(category.text)
from bs4 import BeautifulSoup
import requests

url = "https://www.stroymag-bishkek.com/product-category/metalloprokat/truby-kvadratnyye/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
products = soup.find_all('h2', class_='woocommerce-loop-product__title')
price = soup.find_all('span', class_='price')
print(price)
for product in products:
    print(product.text)
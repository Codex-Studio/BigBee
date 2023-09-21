import os
import random
import psycopg2
import requests
import random
from bs4 import BeautifulSoup
from slugify import slugify
from dotenv import load_dotenv

load_dotenv('.env')

url = "https://www.megamaster.kg/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

# Найдем все элементы, содержащие информацию о продуктах
product_blocks = soup.find_all('div', class_='product-preview__content')

# Создадим список для хранения данных о продуктах
products = []

# Создайте папку media/product_images, если она не существует
if not os.path.exists('media/product_images'):
    os.makedirs('media/product_images')

# Перебираем блоки с продуктами
for block in product_blocks:
    product_name = block.find('div', class_='product-preview__title').text.strip()
    product_price = block.find('span', class_='product-preview__price-cur').text.strip()

    # Убираем лишние символы и пробелы из цены
    product_price = product_price.replace('сом', '').replace(' ', '')

    # Получаем URL изображения из атрибута 'data-src' в теге 'img'
    product_image = block.find('img', class_='lazyload')['data-src']

    # Проверяем, что строка не пуста, прежде чем конвертировать в int
    if product_price:
        current_price = int(product_price)
    else:
        current_price = random.randint(100, 100000)

    # Создаем словарь для текущего продукта и добавляем его в список
    product_data = {
        'title': product_name,
        'price': current_price,
        'image_url': product_image
    }
    products.append(product_data)

print(products)

try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(user=os.environ.get("DB_USER"),
                                  password=os.environ.get("DB_USER_PASSWORD"),
                                  host=os.environ.get("DB_HOST"),
                                  port=os.environ.get("DB_PORT"),
                                  database=os.environ.get("DB_NAME"))

    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    
    # Распечатать сведения о PostgreSQL
    print("Информация о сервере PostgreSQL")
    print(connection.get_dsn_parameters(), "\n")
    
    # Выполнение SQL-запроса
    cursor.execute("SELECT version();")
    
    # Получить результат
    record = cursor.fetchone()
    print("Вы подключены к - ", record, "\n")
    
    for product in products:
        # Преобразуйте название продукта в безопасное имя файла
        print('check')
        file_url = random.randint(111111, 999999)
        image_filename = os.path.join('media', 'product_images', f"{file_url}.jpeg")
        print('work')
        
        # Скачиваем изображение и сохраняем его
        image_url = product['image_url']
        print(image_url)
        image_response = requests.get(image_url)
        with open(image_filename, 'wb') as image_file:
            image_file.write(image_response.content)
        print(image_filename)
        # Вставляем информацию в базу данных
        insert_query = f"""INSERT INTO products_product (title, description, shop_id, category_id, price, image, created) 
        VALUES ('{product['title']}', '{product['title']}', {random.randint(1, 4)}, 
        16, {product['price']}, 'product_images/{file_url}.jpeg', NOW())"""
        cursor.execute(insert_query)

    connection.commit()

except (Exception, psycopg2.Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")

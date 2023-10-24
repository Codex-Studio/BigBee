from bs4 import BeautifulSoup
from slugify import slugify
from dotenv import load_dotenv
import requests
import os
import random
import psycopg2

load_dotenv('.env')

url = "https://stroydvor.kg/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
categories = soup.find_all('div', class_='dark_link')
# print(categories)
for category in categories:
    print(category.text)

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
    
    cursor.execute

    connection.commit()

except (Exception, psycopg2.Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
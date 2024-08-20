# import requests
# from bs4 import BeautifulSoup

# url = 'https://www.freepik.com/popular-photos#from_element=home_verticals'
# response = requests.get(url)

# # with open('index.html', 'w', encoding='utf-8') as file:
# #     file.write(response.text)

# soup = BeautifulSoup(response.text, 'html.parser')

# images = soup.find_all('img')

# for i, img in enumerate(images[:10]):
#     img_url = img.get('src')  # Получаем ссылку на изображение из атрибута src
    
#     # Проверяем, если ссылка неполная (без http), добавляем базовый URL
#     if not img_url.startswith('http'):
#         img_url = url + img_url

#     # Загружаем изображение
#     img_data = requests.get(img_url).content
    
#     # Сохраняем изображение на диск
#     with open(f'image_{i+1}.jpg', 'wb') as img_file:
#         img_file.write(img_data)
    
#     print(f'Изображение {i+1} загружено: {img_url}')

# print("Все изображения загружены.")





# import aiohttp
# import asyncio
# from bs4 import BeautifulSoup

# async def get_image(session, img_url, i):
#     async with session.get(img_url) as response:
#         if response.status == 200:
#             img_data = await response.read()  # Асинхронно получаем содержимое изображения
#             file_name = f'image_{i+1}.jpg'  # Создаем имя файла
#             with open(file_name, 'wb') as img_file:
#                 img_file.write(img_data)  # Сохраняем изображение на диск
#             print(f'Изображение {i+1} загружено: {img_url}')

# async def main():
#     url = "https://www.freepik.com/popular-photos#from_element=home_verticals"

#     # Асинхронный GET-запрос к странице
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             html = await response.text()

#             # Парсинг HTML с использованием BeautifulSoup
#             soup = BeautifulSoup(html, 'html.parser')
#             images = soup.find_all('img')

#             # Лимитируем количество изображений до 10
#             tasks = []
#             for i, img in enumerate(images[:10]):
#                 img_url = img.get('src')

#                 # Если ссылка относительная, добавляем базовый URL
#                 if not img_url.startswith('http'):
#                     img_url = url + img_url

#                 # Добавляем задачу загрузки изображения в список задач
#                 tasks.append(get_image(session, img_url, i))

#             # Асинхронное выполнение всех задач
#             await asyncio.gather(*tasks)

# # Запуск асинхронного цикла
# asyncio.run(main())




import requests
from bs4 import BeautifulSoup

url = ""
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

weather_info = soup.find('div', class_='').get_text()

days_weather = weather_info.split(',')

# Обрабатываем каждую запись
for day in days_weather:
    # Разбиваем каждую запись по пробелам для получения частей строки
    parts = day.strip().split(' ')
    day_of_week = parts[0]          # День недели
    date = parts[1]                 # Дата
    weather = ' '.join(parts[2:])   # Погода

    # Выводим результат
    print(f"День: {day_of_week}, Дата: {date}, Погода: {weather}")

import requests
import json

url = 'https://jsonplaceholder.typicode.com/posts'

response = requests.get(url)
data = response.json()

with open('posts.json', 'w') as file:
    json.dump(data, file)

print("Данные сохранены в файл 'posts.json'")

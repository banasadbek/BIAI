import requests
import json
import csv
import os

urls = ['https://jsonplaceholder.typicode.com/posts','https://jsonplaceholder.typicode.com/comments', 'https://jsonplaceholder.typicode.com/albums', 'https://jsonplaceholder.typicode.com/photos', 'https://jsonplaceholder.typicode.com/todos', 'https://jsonplaceholder.typicode.com/users']

for link in urls:
    response = requests.get(link)
    json_data = response.json()
    headers = json_data[0].keys()
    with open(f"HW7\\{link[link.index('.com/')+5:]}.csv", "wt", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for item in json_data:
            writer.writerow(item.values())

response = requests.get('https://jsonplaceholder.typicode.com/photos')
json_data = response.json()

folder_path = "HW7/images"
os.makedirs(folder_path, exist_ok=True)

for item in json_data:
    image_url = item['url']
    image_id = item['id']
    response = requests.get(image_url)
    if response.status_code == 200:
        image_path = os.path.join(folder_path, f"image_{image_id}.jpg")  # Save as JPG
        with open(image_path, "wb") as f:
            f.write(response.content)
        print(f"Downloaded {image_path}")
    else:
        print(f"Failed to download image {image_id}")







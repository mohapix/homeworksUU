import requests
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import pprint


# Pillow
image = Image.open('../Module10/images/img.jpg')
image = image.resize((1280, 768))
image = image.convert('L')
image = image.rotate(180)
image.show()
image.close()


# matplotlib + numpy
fig, graphx = plt.subplots(figsize=(10, 5.7), layout='constrained')

for i in range(3):
    x = np.random.randint(1, 10)
    y = np.random.randint(1, 10)
    x = np.linspace(0, x)
    y = np.linspace(0, y)
    graphx.plot(x, y, label=f'график {i + 1}')

graphx.set_xlabel('ось X')
graphx.set_ylabel('ось Y')
graphx.set_title("Какой-то график")
graphx.legend()
plt.show()


# requests
URL = 'https://api.github.com/user'
TOKEN = '43095890_some_token_39208439'
USER = 'my_user'
PASSWORD = 'my_password'

response = requests.get(URL, auth=(USER, PASSWORD), params={'access_token': TOKEN, })
response_json = response.json()

print(response.status_code)
print(response.headers['content-type'])
pprint.pprint(response_json)

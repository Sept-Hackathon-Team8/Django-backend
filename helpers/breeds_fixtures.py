import requests
import json

# https://dog.ceo/api/breed/australian/shepherd/images/random
# https://dog.ceo/api/breeds/list/all
API_URL = "https://dog.ceo/api"
IMG_URL = "/breed/"
RAND_IMG = "images/random"

response = requests.get(API_URL + "/breeds/list/all")
json_data = json.loads(response.text)
breeds_data = json_data['message']

main_breeds = list(breeds_data.keys())
data = []

def get_image_and_create_object(breeds, parent=''):
  for breed in breeds:
    img_url = API_URL + IMG_URL + parent + ('/' if parent else '') + breed + '/' + RAND_IMG
    print(img_url)
    response = requests.get(img_url)
    if(response.status_code == 200):
      img_url = json.loads(response.text)['message']
      dog = {'breed': breed, 'parent': parent, 'img_url': img_url }
      data.append(dog)
    if (not parent and breeds_data[breed]):
      get_image_and_create_object(breeds_data[breed], breed)

get_image_and_create_object(main_breeds)

import requests
import json
def sendMotionData(data):
    parajjms = {}
    for i in range(len(data)):
        parajjms['f'+str(i+1)] = data[i]
    parajjms['type'] = "motion"
    response = requests.get('http://127.0.0.1:5000/sendDataFacial', #insert url
                params=parajjms)
    json_response = json.loads(response.text)
    restaurant = json_response['restaurant']
    dish = json_response['dish']
    price = json_response['price']
    size = json_response['size']
    url = json_response['url']
    print(dish)
    print(price)
    print(size)
    print(url)


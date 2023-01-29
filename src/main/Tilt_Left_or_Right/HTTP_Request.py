import requests

def sendMotionData(data):
    parajjms = {}
    for i in range(len(data)):
        parajjms['f'+str(i+1)] = data[i]
    parajjms['type'] = "motion"
    response = requests.get('http://127.0.0.1:5000/sendDataFacial', #insert url
                params=parajjms)
    print(response.url)
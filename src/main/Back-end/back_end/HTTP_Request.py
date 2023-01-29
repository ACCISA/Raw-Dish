import requests

parajjms = {'field1': "1",'field2':0, 'field3':1,'field4':1,'field5':0,'field6':25,'field7':1,'field8':1}
response = requests.get('http://127.0.0.1:5000/sendDataFacial', #insert url
            params=parajjms)
print(response.url)
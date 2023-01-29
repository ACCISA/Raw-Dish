import requests

params = {'field1': '','field2':'', 'field3':'','field4':'','field5':'','field6':'','field7':'','field8':''}
response = requests.get('https://pythonexamples.org/', #insert url instead of this one
            params=params)
print(response.url)
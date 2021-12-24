import requests
import json

def getProcessedDataFromApi(data):
    response_API = requests.post("http://lazt009.pythonanywhere.com/", { "data" : data} )
    if response_API.status_code == 200:
        data = response_API.text
        # print(data)
        return data
    else:
        return None
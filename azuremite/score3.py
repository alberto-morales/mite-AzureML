
from azuremite.deploy_aks import get_service

import pandas as pd
import requests
import json

def init():
    wservice = get_service()
    key1, key2 = wservice.get_keys()
    global scoring_uri, headers
    headers = {'Content-Type':'application/json',
               'Authorization': 'Bearer ' + key1}
    print(headers)
    scoring_uri = wservice.scoring_uri

def run():
    jsonContent = {"columns":[0],"index":[0],"data":[[2000]]}
    print(f"invocaremos con {jsonContent}")
    # make prediction
    resp = requests.post(scoring_uri, json=jsonContent, headers=headers)
    # you can return any data type as long as it is JSON-serializable
    print(resp.status_code)
    print(resp.content)
    return resp.json()

if __name__ == '__main__':
    init()
    prediction = run()
    print(prediction)


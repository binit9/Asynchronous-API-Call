import requests
import json
import os


url = "http://27.0.0.1:5000/status"

status_json = {
               "transaction_id": "XXXXXXXXXX"
           }

response = requests.post(url, json=status_json)
print(response.json())
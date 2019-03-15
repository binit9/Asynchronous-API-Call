import requests
import json
import os

print(os.getcwd())

url = "http://27.0.0.1:5000/receipt"

req_json = {
            "filename": '/home/ubuntu/Policy_2/Restricted Content-Child Endangerment/Restricted Content-Child Endangerment.docx',
            "transaction_id": "XXXXXXXXXX"
        }

response = requests.post(url, json=req_json)
print(response.json())
import requests

headers = {'X-ApiKey':'Your api key would be inserted here','Content-Type': 'application/json;charset=utf-8' }

new_record = {
    "FieldData":{
        "788":"An important string of data",
        "789":"34"
    }
}

r = requests.post('https://api.onspring.com/v1/records/33', headers=headers, json=new_record, verify=False)

print(r.status_code)
print(r.json())
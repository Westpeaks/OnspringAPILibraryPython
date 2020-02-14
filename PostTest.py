import requests

headers = {'X-ApiKey':'5a677cc2bf68c90dcc88234d/b6daea7e-8aba-4373-a5dd-795e4f6cfd95','Content-Type': 'application/json;charset=utf-8' }

new_record = {
    "FieldData":{
        "788":"Stuart Boi",
        "789":"34"
    }
}

r = requests.post('https://api.onspring.com/v1/records/33', headers=headers, json=new_record, verify=False)

print(r.status_code)
print(r.json())
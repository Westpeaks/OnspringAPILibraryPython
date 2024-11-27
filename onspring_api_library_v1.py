# File: Onspring API Python Library
import requests

class HttpHelper:
    def __init__(self, host, header):
        self.host = host
        self.header = header
        
host_key = HttpHelper("https://api.onspring.com", {'X-ApiKey' : 'Your API Key would be inserted here'})

def can_connect():
    host, header = host_key.host, host_key.header   
    response = requests.get(host + '/v1/ping?', headers=header)
    code = response.status_code

    if code == 204:
        print("Your connection is successful!")
    else:
        return response.status_code
    		
def get_apps():
    host, header = host_key.host, host_key.header
    get_list = requests.get(host + '/v1/apps?', headers=header)
    list = get_list.json()
    print(list)

def get_app_fields():
    host, header = host_key.host, host_key.header
    get_fields = requests.get(host + '/v1/fields?appId=14', headers=header)
    fields = get_fields.json()
        
    for field in fields:
        print(field)

def get_app_field():
    host, header = host_key.host, host_key.header
    get_field = requests.get(host + '/v1/fields/292', headers=header)
    field = get_field.json()
    print(field)

def get_app_records():
    host, header = host_key.host, host_key.header
    get_records = requests.get(host + '/v1/records/12', headers=header)
    records = get_records.json()
    
    for record in records:
        print (record)

def get_app_record():
    host, header = host_key.host, host_key.header
    get_record = requests.get(host + '/v1/records/12/4', headers=header)
    record = get_record.json()
    print(record)

def create_app_record():
    host, header = host_key.host, host_key.header
    create_record = requests.post(host + '/v1/records/12', headers=header)
    record = create_record.json()
    print(record)

def update_app_record():
    host, header = host_key.host, host_key.header
    update_record = requests.put(host + '/v1/records/12/4')
    record = update_record.json()
    print(record)

def main():
    create_app_record()

if __name__ == "__main__":
    main()

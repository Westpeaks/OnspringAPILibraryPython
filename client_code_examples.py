import requests

from onspring_api_library_v2 import Onspring

api = Onspring('https://api.onspring.com/','This is where you would insert your api key')

'''List of methods that can be performed'''

# connect = api.can_connect()

# apps = api.get_apps(app_id)

# app_fields = api.get_fields(app_id)

# app_field = api.get_app_field(field_id)

# all_records = api.get_app_records(app_id)

# records = api.get_app_record(app_id, record_id)

# Example data for adding a record.

'''new_record = {
    "FieldData": {
        '788': "Chiefssss!"
        '789': 15
    }
 }'''

# add_record = api.add_app_record(app_id, new_record)

'''add_to_record = {
    "FieldData": {
        '788': "Chiefssss!",
        '789': 15
    }
 }'''

# update_record = api.update_app_record(app_id, record_id, add_to_record)

# delete_record = api.delete_app_record(app_id, record_id)

# Example data for adding attachments
 
'''files = {'file': open('OnspringAPI.pdf', 'rb')}
file_name = "OnspringAPI.pdf"'''

# add_attachment = api.add_attachment(app_id, record_id, field_id, file_name, files=files)

# get_field_attachment = api.get_attachment(app_id, record_id, field_id, file_id) 

# reports = api.get_reports(app_id)

# report_data = api.get_report_data(report_id)



'''To try your code, copy one of the methods, remove it from comments, and input the appropriate data'''

# Example - Try your code here

connect = api.can_connect()

print(connect)
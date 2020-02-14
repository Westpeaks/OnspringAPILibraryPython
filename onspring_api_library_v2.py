import requests
import json

class Onspring:

    ## INITIALIZATION (Constructor and Objects)##
    
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.header = {'X-ApiKey': api_key}

    def _get(self, path):
        return requests.get(self.base_url + path, headers=self.header).json()

    def connect_get(self, path):
        return requests.get(self.base_url + path, headers=self.header)

    def _post(self, path, body):
        return requests.post(self.base_url + path, headers=self.header,json=body).json()

    def _attach(self, path, files):
        return requests.post(self.base_url + path, headers=self.header,files=files)    

    def _put(self, path, body):
        return requests.put(self.base_url + path, headers=self.header,json=body).json()

    def _delete(self, path):
        return requests.delete(self.base_url + path, headers=self.header).json()

    def can_connect(self):
        response = self.connect_get('/ping')
        code = response.status_code

        if code == 204:
            return("Your connection is successful!")
        else:
            return (code)


    ## REST FUNCTIONS (Methods) ##        

    def get_apps(self):
        return self._get('/apps?')

    def get_fields(self, app_id):
        return self._get('/fields?appId={}'.format(app_id))

    def get_app_field(self, field_id):
        return self._get('/fields/{}'.format(field_id))

    def get_app_records(self, app_id):
        return self._get('/records/{}'.format(app_id))

    def get_app_record(self, app_id, record_id):
        return self._get('/records/{}/{}'.format(app_id, record_id))

    def add_app_record(self, app_id, body):
        return self._post('/records/{}'.format(app_id), body)

    def update_app_record(self, app_id, record_id, body):
        return self._put('/records/{}/{}'.format(app_id, record_id), body)

    def delete_app_record(self, app_id, record_id):
        return self._delete('/records/{}/{}'.format(app_id, record_id))

    def add_attachment(self, app_id, record_id, field_id, file_name, files):
        return self._attach('/files/{}/{}/{}?fileName={}'.format(app_id, record_id,field_id, file_name), files)

    def get_attachment(self, app_id, record_id, field_id, file_id):
        return self.connect_get('/files/{}/{}/{}?fileId={}'.format(app_id, record_id,field_id, file_id))

    def get_reports(self, app_id):
        return self._get('/reports?appId={}'.format(app_id))

    def get_report_data(self, report_id):
        return  self._get('/reports/{}?dataType=ReportData&dataFormat=Raw'.format(report_id))

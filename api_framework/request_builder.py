# api_framework/request_builder.py
import requests

class RequestBuilder:
    def __init__(self):
        self.url = None
        self.headers = {}
        self.params = {}
        self.data = None
        self.files = None
        self.method = "GET"

    def set_url(self, url):
        self.url = url
        return self

    def add_header(self, key, value):
        self.headers[key] = value
        return self

    def set_data(self, data):
        self.data = data
        return self

    def add_file(self, key, file):
        if self.files is None:
            self.files = {}
        self.files[key] = file
        return self

    def set_method(self, method):
        self.method = method
        return self

    def build(self):
        if self.method.upper() == "GET":
            return requests.get(self.url, headers=self.headers, params=self.params)
        elif self.method.upper() == "POST":
            return requests.post(self.url, headers=self.headers, json=self.data,files=self.files)
        elif self.method.upper() == "PUT":
            return requests.put(self.url, headers=self.headers, json=self.data)
        elif self.method.upper() == "DELETE":
            return requests.delete(self.url, headers=self.headers, params=self.params)
        else:
            raise ValueError("Unsupported HTTP method")

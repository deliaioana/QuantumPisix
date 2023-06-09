import requests


class Request:
    url = "http://localhost:8082"

    def __init__(self, params):
        self.params = params

    def send_request(self):
        response = requests.get(url=self.url)
        data = response.json()
        return data

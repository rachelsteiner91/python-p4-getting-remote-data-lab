import requests
import json



class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
    ##module get_response_body function returns response.
        response = requests.get(self.url)
        return response.content

    ##module load_json function returns response.
    def load_json(self):
        return json.loads(self.get_response_body())
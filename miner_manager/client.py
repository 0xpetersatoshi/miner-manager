"""
API client wrapper.
"""
import requests

BASE_URL = 'https://ethgasstation.info/api/ethgasAPI.json'

class Client4xxError(Exception):
    pass

class Client5xxError(Exception):
    pass

class Client429Error(Exception):
    pass

class APIClient:
    base_url = BASE_URL
    
    def __init__(self, api_key) -> None:
        self._api_key = api_key
        self.session = requests.Session()
        self.headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'python3.6',
        }

    def make_request(self, method, url):
        with self.session as session:
            response = session.request(method, url, headers=self.headers)

        if response.status_code >= 500:
            raise Client5xxError

        if response.status_code == 429:
            raise Client429Error

        if response.status_code != 200:
            raise Client4xxError

        return response.json()

    def get(self):
        return self.make_request('GET', self._build_url())

    def _build_url(self):
        return f'{self.base_url}?api-key={self._api_key}'

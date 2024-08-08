import requests


class APIClient:
    def __init__(self):
        self.base_url = "https://api.test.idnow.de"

    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        print(f"GET: {url}")  # Debug logging
        response = requests.get(url, params=params)
        print(f"Response: {response.status_code}, {response.text}")  # Debug logging
        response.raise_for_status()
        return response.json()

    def post(self, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        print(f"POST: {url}")  # Debug logging
        response = requests.post(url, json=data)
        print(f"Response: {response.status_code}, {response.text}")  # Debug logging
        response.raise_for_status()
        return response.json()

    def put(self, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        print(f"PUT: {url}")  # Debug logging
        response = requests.put(url, json=data)
        print(f"Response: {response.status_code}, {response.text}")  # Debug logging
        response.raise_for_status()
        return response.json()

    def delete(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        print(f"DELETE: {url}")  # Debug logging
        response = requests.delete(url, params=params)
        print(f"Response: {response.status_code}, {response.text}")  # Debug logging
        response.raise_for_status()
        return response.json()

import requests

class ApiCall:
    def __init__(self, end, para=None):
        self.resp = requests.get(url=end, params=para)
        self.data = self.resp.json()

    def api_req(self):
        self.resp.raise_for_status()
        return self.data
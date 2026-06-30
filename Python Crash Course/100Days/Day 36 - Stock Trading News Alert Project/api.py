import requests
import requests_cache
from requests_cache import CachedSession


class ApiCall:
    def __init__(self, end, para=None):
        session = CachedSession('maxcache', expire_after=86400)
        self.resp = session.get(url=end, params=para)
        self.data = self.resp.json()

    def api_req(self):
        self.resp.raise_for_status()
        return self.data
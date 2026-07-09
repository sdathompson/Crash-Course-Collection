import requests

from requests_cache import CachedSession

class ApiCall:
    def __init__(self, end=None, para=None):
        session = CachedSession('maxcache', expire_after=86400)
        if end is not None:
            self.resp = session.get(url=end, params=para)
            self.data = self.resp.json()


    def api_req(self):
        self.resp.raise_for_status()
        return self.data

    def api_post(self, end, para, head=None, receipt=True):
        if head is not None:
            self.resp = requests.post(url=end, json=para, headers=head)
        else:
            self.resp = requests.post(url=end, json=para)

        if receipt:
            print(self.resp.text)

    def api_put(self, end, para, head=None, receipt=True):
        if head is not None:
            self.resp = requests.put(url=end, json=para, headers=head)
        else:
            self.resp = requests.put(url=end, json=para)

        if receipt:
            print(self.resp.text)

    def api_delete(self, end, para=None, head=None, receipt=True):
        if head is not None and para is not None:
            self.resp = requests.delete(url=end, json=para, headers=head)
        if head is not None:
            self.resp = requests.delete(url=end, headers=head)
        else:
            self.resp = requests.delete(url=end, json=para)

        if receipt:
            print(self.resp.text)
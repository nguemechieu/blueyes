import json
from urllib import request, response


class RequestHandler(object):
    def __init__(self, requests, api_key, url0):
        self.request = requests
        self.url = url0
        self.api_key = api_key


def make_request(method0: object, api_key: str, urls: str, data0: str = None) -> json:
    r = request.urlopen(url =urls, data=data0, cadefault=False, capath='', timeout=5000)
    r.add_header("Authorization", "Bearer " + api_key)
    r.add_header("Content-Type", "application/json")
    r.add_header("Accept", "application/json")

    print("response ", response)
    return json.loads(r.read())

import json
import logging
from urllib import request, response

import requests


class RequestHandler(object):
    def __init__(self,  api_key, url0):

        self.url0 = url0
        self.api_key = api_key



    def make_request(self,path) -> json:
     r = requests
     data=r.get(url=self.url0+path,params=None,headers={  'Content-Type' : 'application/json','Authorization' : 'Bearer ' + self.api_key}
           ,timeout=5000,allow_redirects=True,stream=True,verify=True)


     if data.status_code!=200:
         logging.error("Error creating request"+ data.text)

         print("Error creating request status code ="+ data.status_code .__str__()+ data.text)
     else: print('Request created successfully '+ data.text)


     return json.loads(data.text)

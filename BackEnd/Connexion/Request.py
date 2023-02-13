
import logging
from urllib import request
class RequestHandler(object):
  
 def __init__(self, request):
     self.request = request

def makeRequest ( url , method)->object: 
 request.method = method
 request.url = url
 request.method = method
 r = request.urlopen(request.url)
 request.Request.add_header('Content-Type', 'application/json')
 request.Request.add_header('Accept', 'application/json')
 response=r.read()
 print("response ",response )

 return response

mq= makeRequest("https://api.binance.us/api/v3/trades?symbol=LTCBTC", "GET")
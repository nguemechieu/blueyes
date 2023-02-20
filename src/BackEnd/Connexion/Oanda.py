from datetime import datetime

from src.BackEnd.Connexion.RequestHandler import RequestHandler

api_key0 ='717fdd7e14f3e5e408f679517dc00307-857852225e99895c667f3889c65e9ef1'
account_id='001-001-2783446-006'


class Oanda:

 def __init__(self, account_id_, api_key):

        self.api_key = api_key
        self.account_id = account_id_

        self.req=RequestHandler(api_key=api_key0,url0='https://api-fxtrade.oanda.com')

 def create(self): return
 def trade(self): return
 def order(self): return
 def run(self): return
 def update(self): return


 def get_candles_data (self,instrument:str =None, granularity_= None)->object:
       granularity0=granularity_
       pat= "/v3/instruments/"+instrument+"/candles?count=10&price=A&from=2016-01-01T00%3A00%3A00.000000000Z&granularity="+granularity0
       data=self.req.make_request(path=pat)
       return data
 def get_account(self ):
       da=self.req.make_request(path='/v3/account/'+account_id)

       return da

 def get_order_book(self, instrument:str =None):
       path_="v3/instruments/"+instrument+"/orderBook"

       return self.req.make_request(path=path_)
 def get_position_book(self, instrument:str =None):
       path_='/v3/instruments/'+instrument+'/positionBook'

       return self.req.make_request(path=path_)

 def create_market_order(self, instrument:str =None,units:int=100):

        path_="/v3/accounts/" +account_id+"/orders?units="+str(units)+"&instrument="+instrument+"&timeInForce=FOK&type=MARKET&positionFill=DEFAULT"
        return  self.req.make_request(path=path_)


 def create_pendings_order(self, instrument:str =None,units:int=100):

         path_="/v3/accounts/" +account_id+"/pendingOrders?units="+str(units)+"&instrument="+instrument+"&timeInForce=FOK&type=MARKET&positionFill=DEFAULT"
         return  self.req.make_request(path=path_)
   #     "createTime": "2016-06-22T18:41:29.294265338Z",
   # "id": "6375",
   # "instrument": "EUR_CAD",
   # "partialFill": "DEFAULT_FILL",
   # "positionFill": "POSITION_DEFAULT",
   # "price": "1.30000",
   # "replacesOrderID": "6373",
   # "state": "PENDING",
   # "timeInForce": "GTC",
   # "triggerCondition": "TRIGGER_DEFAULT",
   # "type": "MARKET_IF_TOUCHED",
   # "units": "10000"








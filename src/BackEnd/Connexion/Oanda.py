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


   def get_candles_data (self,instrument:str =None)->object:

       data=self.req.make_request(path='/v3/instruments/'+instrument+'/candles')


       return data

   def get_account(self ):
       da=self.req.make_request(path='/v3/account/'+account_id)

       return da

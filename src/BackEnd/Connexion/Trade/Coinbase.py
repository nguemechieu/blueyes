
class Coinbase(object):
    def __init__(self, *args, **kwargs):
     self.amount = kwargs.pop('amount','')
     self.currency = kwargs.pop('currency','')

    def __str__(self): return 
    
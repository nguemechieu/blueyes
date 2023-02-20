import logging

from src.BackEnd.Connexion.RequestHandler import RequestHandler

api_key_binance= ''

logger = logging.getLogger(__name__)
class BinanceUs:
    def __init__(self, api_key):
        self.api_key = api_key


def create() -> bool:
    req = RequestHandler(url0="https://api.binance.us", api_key=api_key_binance)

    rw = req.make_request('/klines')
    if rw is None: return False


def trade(): return


def order(): return


def run(): return


def update(): return

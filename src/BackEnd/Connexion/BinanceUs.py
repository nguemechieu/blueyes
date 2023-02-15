import RequestHandler


class BinanceUs:
    def __init__(self, api_key):
        self.api_key = api_key


def create() -> bool:
    req = RequestHandler

    rw = req.make_request("https://api.binance.us", "POST", "2345456fgh", url)
    if rw is None: return False


def trade(): return


def order(): return


def run(): return


def update(): return

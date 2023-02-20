import pandas as pd


class CoinbasePro:
    def __init__(self, api_key, username, password, api_secret, pass_phrase):
        self.user = username
        self.password = password
        self.api_key = api_key
        self.api_secret = api_secret
        self.pass_phrase = pass_phrase

def get_time_frame_list():

    data=[pd.read_csv('oanda__granularity.csv')]

    data1=data.__getattribute__('Value')
    print ('data = ' + data1)

    return data1

def create(): return


def trade(): return


def order(): return


def run(): return


def update(): return

# File to create a quick, easy DataFrame using BTC's hourly 2019 prices
import pandas as pd


def demo_df(url=None):
    if url is None:
        url = "https://raw.githubusercontent.com/carlfarterson/TAcharts/master/data/btc.csv"

        _demo_df = pd.read_csv(url)
    print("Download")
    return _demo_df

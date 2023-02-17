import matplotlib.pyplot as plt
import pandas as pd

from numpy import double


class CandleStickChart(object):
    def __init__(self, root):
        self.root = root

        # create figure
        plt.cbook.GrouperView(self.root)

        # define width of candlestick elements
        width = .4
        width2 = .05

        # define up and down prices

        # create DataFrame

        prices0 = pd.read_csv("btc-prices.csv")
        date = prices0['Date']
        open_: double
        open_ = prices0['Open']
        high: double
        high = prices0['High']
        low: double
        low = prices0['Low']
        close_: double
        close_ = prices0['Close']
        volume = prices0['Volume']
        openvar = [35, 22, 21, 19, 23, 21, 25, 29]
        highvar = [79, 20, 17, 23, 22, 25, 29, 31]
        lowvar = [8, 27, 29, 25, 24, 26, 31, 37]
        closevar = [89, 16, 14, 17, 19, 18, 22, 26]

        prices = pd.DataFrame({'Open': openvar,
                               'Close': closevar,
                               'High': highvar,
                               'Low': lowvar},
                              index=pd.date_range("2015-01-01", periods=8, freq="d"))

        # define up and down prices
        up = prices[prices.Close >= prices.Open]
        down = prices[prices.Close < prices.Open]
        print(prices)
        # display DataFrame

        # define colors to use
        col1 = 'green'
        col2 = 'red'

        # plot up prices
        plt.bar(up.index, up.Close - up.Open, width, bottom=up.Open, color=col1)
        plt.bar(up.index, up.High - up.Close, width2, bottom=up.Close, color=col1)
        plt.bar(up.index, up.Low - up.Open, width2, bottom=up.Open, color=col1)

        # plot down prices
        plt.bar(down.index, down.Close - down.Open, width, bottom=down.Open, color=col2)
        plt.bar(down.index, down.High - down.Open, width2, bottom=down.Open, color=col2)
        plt.bar(down.index, down.Low - down.Close, width2, bottom=down.Close, color=col2)

        # rotate x-axis tick labels
        plt.xticks(rotation=45, ha='right')
        plt.show()

        # display candlestick chart

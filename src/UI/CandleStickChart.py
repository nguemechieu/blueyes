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
        prices = pd.read_csv("btc-prices.csv")
        date = prices['Date']
        open_: double = prices['Open']
        high: double= prices['High']
        low: double = prices['Low']
        close_: double= prices['Close']
        volume = prices['Volume']
        openvar = [20, 22, 21, 19, 23, 21, 25, 29]
        highvar = [31, 20, 17, 23, 22, 25, 29, 31]
        lowvar = [13, 27, 29, 25, 24, 26, 31, 37]
        closevar = [30, 16, 14, 17, 19, 18, 22, 26]

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
        plt.xticks(rotation=35, ha='right')
        plt.scatter(up.index, up.Close - up.Open)

        plt.title('Market Data')
        plt.xlabel('Time')
        plt.ylabel('Price')

        plt.show()

        # display candlestick chart

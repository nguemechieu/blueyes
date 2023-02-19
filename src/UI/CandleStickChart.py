import csv
import json
from tkinter import Canvas

import matplotlib.pyplot as plt
import pandas as pd

from src.BackEnd.Connexion.Oanda import Oanda, account_id, api_key0


def get_xscroll_command()->str:
    return 'xscroll'



def get_yscroll_command()->str:
    return 'yscroll'


class CandleStickChart(object):
    def __init__(self, root):
        global outfile
        self.root = root

        # create figure
        plt.figure(facecolor='black',edgecolor='white')
        plt.xlabel("Candle-Stick")

        canvas=Canvas(master=root,takefocus=3,bg='black',borderwidth=1000,border=12,width=1000,height=500,selectbackground='blue')


        canvas.pack()
        # define width of candlestick elements
width = .4
width2 = .05


#Getting data from Api

# Display the Candle sticks chart
r= Oanda(account_id_=account_id,api_key=api_key0)
data=r.get_candles_data('EUR_USD')

with open("data.json", "w") as outfile:
    json.dump(data, outfile,sort_keys=True,indent=2)

with open('data.json') as json_file:
    dat= json.load(json_file)

d= dat



# now we will open a file for writing
data_file = open('data.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(data_file)

# Counter variable used for writing
# headers to the CSV file
count = 0

symbol= d['instrument']
granularity= d['granularity']

candle=d['candles']



with open("data1.json", "w") as outfile: json.dump(candle, outfile,sort_keys=True,indent=2)
with open('data1.json') as json_file: data_= json.load(json_file)

date =''
mid:object=None
# Extracting candle data from json file data1.json
for i in data_:
    complete= i.get('complete')
    print(" complete "+ complete.__str__())
    mid= i.get('mid')
    print(" mid " + mid.__str__())
    date= i.get('time')

# Writing new  candle data from json file data1.json to file data2.json
with open("data2.json", "w") as outfile0: json.dump(mid, outfile0,sort_keys=True,indent=2)
## Loading new data from json file data2.json
with open('data2.json') as json_file: mid1= json.load(json_file)
# Creating candle parameters
xopen:float=0.1
xclose:float=0
xhigh:float=0
xlow:float=0



# Adding values to candle parameters
for j, value in mid1.items():
    print(j, value)

    if j == 'o':
        xopen=value

    if j == 'h':
        xhigh=value
    if j == 'l':
        xlow=value
    if j == 'c':

        xclose=value


# Saving data to list params
open_list=[xopen]

high_list =[xhigh]
low_list=[xlow]
close_list =[xclose]



# Writing data to CSV

# data rows of csv file
avg =5.7
direction =''
down:float=2.2
up:float=2.1
mydict  = [{'Date':date,'Open':xopen,'High':xhigh,'Low':xlow,'Close':xclose,'avg':avg,'direction':direction,'up':up,'down':down}]

# field names
fields = ['Date', 'Open', 'High', 'Low','Close','avg','direction','up','down']

# name of csv file

filename = "data3.csv"
# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv dict writer object
    writer = csv.DictWriter(csvfile, fieldnames = fields)

    # writing headers (field names)
    writer.writeheader()

    # writing data rows
    writer.writerows(mydict)




openvar = open_list
highvar = high_list
lowvar = low_list
closevar = close_list



print(open_list + high_list + low_list + close_list)

prices=pd.read_csv('data3.csv')

# define up and down prices



up = prices[prices.Close >=prices.Open]
down = prices[prices.Open < prices.Open]

print(prices)
prices=pd.DataFrame({'Open': openvar,
                     'Close': closevar,
                     'High': highvar,
                     'Low': lowvar},
                    index=pd.date_range("2015-02-17", periods=8, freq="d"))

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
plt.hist(up.index, color='red',label='Histogram')
plt.scatter(up.index, up.Close - up.Open)
plt.title('Pairs of '+symbol)
plt.xlabel('Time'+ date)
plt.ylabel('Price')
plt.show()
# display candlestick chart
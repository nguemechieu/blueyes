import csv
import json
import tkinter
from tkinter import Canvas

import matplotlib.pyplot as plt
import pandas as pd
import self as self

from src.BackEnd.Connexion.Oanda import Oanda, account_id, api_key0


def get_xscroll_command()->str:
    return 'xscroll'

def get_yscroll_command()->str:
    return 'yscroll'

class CandleStickChart(object):
   def __init__(self, root):
        global outfile
        self.root = root
        # define width of candlestick elements

        canvas=Canvas(master=self.root,takefocus=3,bg='black',borderwidth=1000,border=12,width=1000,height=500,selectbackground='blue')
        canvas.pack()


open_list :list=list()
close_list:list=list()
high_list:list=list()
low_list:list=list()


#Getting data from Api
# Display the Candle sticks chart


r_= Oanda(account_id_=account_id, api_key=api_key0)
data__=r_.get_candles_data('EUR_USD', granularity_='D')
with open("data.json", "w") as outfile:
    json.dump(data__, outfile, sort_keys=True, indent=2)

with open('data.json') as _json_file:
    dat= json.load(_json_file)
    # now we will open a file for writing
    data_file = open('data.csv', 'w')
    # create the csv writer object
    csv.writer(data_file)
    # Creating candle parameters

         # create figure
plt.figure(facecolor='black',edgecolor='white')

plt.xlabel("Candle-Stick")

width = .4
width2 = .05

# Display the Candle sticks chart
r= Oanda(account_id_=account_id,api_key=api_key0)
while True:
 data: object=r.get_candles_data('EUR_USD',granularity_='D')
 xopen:float=0.1
 xclose:float=0
 xhigh_:float=0
 xlow:float=0
 symbol=data ['instrument']
 granularity= data ['granularity']
 candle=list(data['candles'])
 with open("data1.json", "w") as outfile: json.dump(candle, outfile,sort_keys=True,indent=2)
 with open('data1.json') as json_file: data_= json.load(json_file)

 date =''
 mid:object=None
 # Extracting candle data from json file data1.json
 for i in data_:
    complete= i.get('complete')
    print(" complete "+ complete.__str__())
    mid= i.get('ask')
    print(" ask " + mid.__str__())
    date= i.get('time')
    # Writing new  candle data from json file data1.json to file data2.json
    with open("data2.json", "w") as outfile0: json.dump(mid, outfile0,sort_keys=True,indent=2)
    ## Loading new data from json file data2.json
    with open('data2.json') as json_file: mid1= json.load(json_file)

 # data rows of csv file
 avg =5.7
 direction =''
 down:float=2.2
 up:float=2.1
 xhigh_:float
 # Adding values to candle parameters
 for k in data_ :
  for j, value in mid1.items():

       print(j, value)
       if j == 'o':
         xopen=value

       if j == 'h':
         xhigh_=value

       if j == 'l':
           xlow=value

       if j == 'c':
           xclose=value


       open_list=[xopen]
       high_list=[xhigh_]
       low_list=[xlow]
       close_list=[xclose]

       volume_list=k['volume']
       print('volume ' + str(volume_list))


       print('k ' + str(k))



# Saving data to list params
# json_to_csv('data1.json','data1.csv')


 mydict  = {'Date':date,'o':xopen,'h':xhigh_,'l':xlow,'c':xclose,'avg':avg,'direction':direction,'up':up,'down':down}
 with  open("data2.json", "w") as outfile:
       json.dump(mydict, outfile,sort_keys=True,indent=2)
# Writing data to CSV

 with open('data2.json') as json_file: data_= [json.load(json_file)]
# openvar = [25, 22, 21, 19, 23, 21, 25, 29]
# highvar = [15, 20, 17, 23, 22, 25, 29, 31]
# lowvar = [12, 27, 29, 25, 24, 26, 31, 37]
# closevar = [23, 16, 14, 17, 19, 18, 22, 26]
 prices= pd.read_csv("data2.csv")
 print("Data  " +"o "+str(open_list)+ " " +"v "+str(close_list)+ " " +str(high_list)+ " " +str(low_list)+ "")
 pd.DataFrame({
    "Date": [date],
    "avg": [avg],
    "c": [23, 16, 14, 17, 19, 18, 22, 26],
    "direction": direction,
    "down": down,
    "h": [15, 20, 17, 23, 22, 25, 29, 31],
    "l": [12, 27, 29, 25, 24, 26, 31, 37],
    "o": [25, 22, 21, 19, 23, 21, 25, 29],
    "up": up},
                      index=pd.date_range("2015-01-01", periods=8, freq="d"))



 up = prices[prices.c >=prices.o]
 down = prices[prices.o < prices.o]
 print(prices)


 print(open_list + high_list + low_list + close_list)
# # display DataFrame
#
# # define colors to use
 col1 = 'green'
 col2 = 'red'
 plt.bar(up.index, up.c - up.o, width, bottom=up.o, color=col1)
 plt.bar(up.index, up.h - up.c, width2, bottom=up.c, color=col1)
 plt.bar(up.index, up.l - up.o, width2, bottom=up.o, color=col1)
 # plot down prices
 plt.bar(down.index, down.c - down.o, width, bottom=down.o, color=col2)
 plt.bar(down.index, down.h - down.o, width2, bottom=down.o, color=col2)
 plt.bar(down.index, down.l - down.c, width2, bottom=down.c, color=col2)
 # rotate x-axis tick labels
 plt.xticks(rotation=35, ha='right')
 plt.hist(up.index, color='red',label='Histogram')
 plt.scatter(up.index, up.c - up.o)
 plt.title('Pairs of '+symbol)
 plt.xlabel('Time'+ date)
 plt.ylabel('Price')
 plt.legend(loc='upper left')
 #print('pending order '+ str(r_.create_pendings_order('EUR_USD',1000)))
 #print('Market  order status'+ str(r_.create_market_order(instrument='EUR_USD',units=1000)).capitalize())

 plt.show()




  # # display candlestick chart
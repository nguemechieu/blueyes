import  tkinter as tk
import datetime
class MainWindow(object):

    def __init__(self, window):
     self.window = window

           
    def show ():       
          window=tk.Tk()
          window.title("Blueyes")
          window.geometry("1500x700")
          

          newlabel=tk.Label(text="Starting server now " + datetime.datetime.now().strftime("%Y-%m-%d %H:%d %M:%S %Z"))
          newlabel.grid(column=2,row=3)

          window.mainloop()
     
          print ("Starting server now " + datetime.datetime.now().strftime("%Y-%m-%d %H:%d %M:%S %Z"))      
          return
    
    
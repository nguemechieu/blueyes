


from tkinter.dialog import Dialog


class TradingWindow(Dialog):


 def __init__(self, **kwargs):
    self.info = kwargs.pop('info', None)
    self.title = kwargs.pop('title', None)
  
  

def show(s):
    dialog=Dialog()


    dialog.pack()  
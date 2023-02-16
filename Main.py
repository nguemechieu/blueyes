import logging
import tkinter
from doctest import master

from Bueyes.src.UI.LoginFrame import LoginFrame

# Create and configure logger
logging.basicConfig(filename="newfile.log", format='%(asctime)s %(message)s', filemode='w')
# Creating an object
logger = logging.getLogger(__name__)
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)


# Defining main function
def main():
    if __name__ == '__main__':
        root = tkinter.Tk()
        root.iconify = True
        root.resizable = True
        root.image_names = ['blueyes.png']
        root.iconbitmap('../Bueyes/src/images/blueyes.ico')
        bgf = tkinter.PhotoImage(file='../Bueyes/src/images/blueyes.png')

        # Adjust size
        root.geometry("1530x780")
        return LoginFrame(root=root, bgf=bgf)



# Using the special variable
# __name__
if __name__ == "__main__":
    main().mainloop()


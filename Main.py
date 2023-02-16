import logging
import tkinter

from Bueyes.src.UI.LoginFrame import LoginFrame, show_pages

# Create and configure logger
logging.basicConfig(filename="blueyes.log", format='%(asctime)s %(message)s', filemode='w')

# Creating an object
logging.getLogger(__name__)

# Using the special variable
# __name__
if __name__ == "__main__":

    show_pages('Login')

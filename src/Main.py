
import logging

from src.UI.LoginFrame import show_pages
from src.UI.News import News

# Create and configure logger
logging.basicConfig(filename="blueyes.log", format='%(asctime)s %(message)s', filemode='w')
# Creating an object
__name___ = 'LoginFrame'

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

news=News()
news.get()

# Using the special variable
# __name__
if __name__ == "__main__":
 logger.debug("Blueyes is starting...")

 show_pages('Login')
 curses.endwin() #Close screen

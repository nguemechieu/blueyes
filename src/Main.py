import logging
import sys
from src.UI.LoginFrame import show_pages
# Create and configure logger
logging.basicConfig(filename="blueyes.log", format='%(asctime)s %(message)s', filemode='w')

# Creating an object
__name___ = 'LoginFrame'
logging.getLogger(__name___)

# Using the special variable
# __name__
if __name__ == "__main__":
  logging.info('Creating a new LoginFrame')
  show_pages('Login')
else: # __main__ is not defined

    logging.info('Main is exiting')

    sys.exit()

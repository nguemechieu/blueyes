import logging

from Bueyes.src.UI.MainWindow import MainWindow
from Bueyes.src.UI.News import News

# Create and configure logger
logging.basicConfig(filename="newfile.log", format='%(asctime)s %(message)s', filemode='w')
# Creating an object
logger = logging.getLogger(__name__)
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)


# Defining main function
def main():
    main0 = MainWindow()
    main0.show()


# Using the special variable
# __name__
if __name__ == "__main__":

    main()



import logging
from Bueyes.src.UI.MainWindow import MainWindow
# Create and configure logger
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)
# Creating an object
# opts, args = getopt.getopt(sys.argv,"?hH")


def main() -> None:
    app = MainWindow

    app.MainWindow.show()

    # Test messages

    return


# Starting Application


main()
logger.debug("Harmless debug Message")
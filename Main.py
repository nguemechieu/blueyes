import logging
from UI import MainWindow


# Creating an object
# opts, args = getopt.getopt(sys.argv,"?hH")
class Main(object): pass


logger = logging.getLogger(__name__)


def main() -> None:
    mainMenu = MainWindow
    mainMenu.MainWindow.show()
    return


mains = main()

import logging

from Bueyes.src.UI.MainWindow import MainWindow

# Creating an object
# opts, args = getopt.getopt(sys.argv,"?hH")

logger = logging.getLogger(__name__)


def main() -> None:
    main_menu = MainWindow
    main_menu.MainWindow.show()
    logger.log()
    return


main()

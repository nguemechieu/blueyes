from mysql.connector import MySQLConnection, Error

from Bueyes.src.BackEnd.configparser.ConfigParser import read_db_config


class Db(object):

    def __init__(self, started, host, port, database, user, password):
        self.started = started
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password

    @classmethod
    def connect(cls) -> None:
        return connect()


def connect():
    """ Connect to MySQL database """

    db_config = read_db_config()
    conn = None
    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print('Connection established.')
        else:
            print('Connection failed.')

    except Error as error:
        print(error)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Connection closed.')



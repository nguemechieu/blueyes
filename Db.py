import self
from mysql.connector import MySQLConnection, Error

from Bueyes.src.BackEnd.configparser.ConfigParser import read_db_config


class Db(object):

    def __init__(self):
        self.conn1 = None

    def connexion(self, conn1=None):
        self.conn1 = conn1
        """ Connect to MySQL database """

        try:
            print('Connecting to ' + read_db_config().get('database') + ' database...')

            conn1: MySQLConnection = MySQLConnection(**read_db_config())

            if conn1.is_connected():
                print('Connection established.')
                return conn1
            else:
                print('Connection failed.')

        except Error as error:
            print(error)

        finally:
            if conn1 is not None and conn1.is_connected():
                conn1.close()
                print('Connection closed.')

    def execute(self, param):

        self.connexion().cmd_stmt_execute(statement_id=self.conn1, data=param, flags=0)

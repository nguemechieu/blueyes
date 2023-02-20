import logging

from mysql.connector import MySQLConnection, Error
from src.BackEnd.configparser.ConfigParser import read_db_config

logging.basicConfig(filename="blueyes.log", format='%(asctime)s %(message)s', filemode='w')

class Db:
    def __init__(self):
        self.conn1 = False
    def connexion(self, conn1=None):
        self.conn1 = conn1
        """ Connect to MySQL database """

        try:
            print('Connecting to ' + read_db_config().get('database') + ' database...')

            conn1: MySQLConnection = MySQLConnection(**read_db_config())

            if conn1.is_connected():
                print('Connection established.')
                logging.info('Connected to database')
                return conn1
            else:
                print('Connection failed.')
                logging.info('Connection failed')

        except Error as error:
            print(error)

        finally:
            if conn1 is not None and conn1.is_connected():
                conn1.close()
                print('Connection closed.')
                logging.info('Connection closed')

    def execute(self, param):

        self.connexion().cmd_stmt_execute(statement_id=self.conn1, data=param, flags=0)

    @classmethod
    def commit(cls):
        cls.connexion().commit()
        pass

import self
from mysql.connector import MySQLConnection, Error

from Bueyes.src.BackEnd.configparser.ConfigParser import read_db_config


class Db(object):

    @staticmethod
    def connect() -> object:
        """ Connect to MySQL database """

        global conn1
        db_config = read_db_config()

        try:
            print('Connecting to '+db_config.get('database')+' database...')

            conn1 = MySQLConnection(**db_config)

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

    @classmethod
    def commit(cls):
        conn1.commit()

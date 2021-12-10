import pymysql
from settings import *


class cur:
    def __enter__(self):
        self.connect = pymysql.Connect(host=HOST,
                                       port=DB_PORT,
                                       user=DB_USER,
                                       passwd=DB_PASSWORD,
                                       db=DB,
                                       cursorclass=pymysql.cursors.DictCursor)
        return self.connect.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connect.commit()
        self.connect.close()
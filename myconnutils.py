import pymysql.cursors


def getConnection():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='*******',
                                 db='flask_mysql',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection
